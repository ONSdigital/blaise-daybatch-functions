from copy import deepcopy
from unittest import mock

from behave import given, then, when

from main import create_daybatches

mock_installed_instrument_data_template = {
    "surveyDays": [
        "2021-01-01T01:01:01.999Z"
    ],
    "name": "",
    "id": "12345-12345-12345-12345-XXXXX",
    "serverParkName": "gusty",
    "installDate": "2021-01-01T01:01:01.999Z",
    "status": "Active",
    "activeToday": None,
    "dataRecordCount": None,
    "hasData": True,
    "nodes": [
        {
            "nodeName": "blaise-gusty-mgmt",
            "nodeStatus": "Active"
        },
        {
            "nodeName": "blaise-gusty-data-entry-1",
            "nodeStatus": "Active"
        },
        {
            "nodeName": "blaise-gusty-data-entry-2",
            "nodeStatus": "Active"
        }
    ]
}


def mock_create_daybatch(context):
    def mock_function(_config, instrument):
        context.created_daybatches[instrument] = 1

    return mock_function


@given("there are no instruments installed")
def step_impl(context):
    with mock.patch("main.get_installed_instrument_data") as mock_get_installed_instrument_data:
        mock_get_installed_instrument_data.return_value = []


@when("the create daybatch process is triggered")
def step_impl(context):
    if not hasattr(context, "created_daybatches"):
        context.created_daybatches = {}
    with mock.patch("main.get_installed_instrument_data") as mock_get_installed_instrument_data:
        mock_get_installed_instrument_data.return_value = context.installed_instrument_data.values()
        with mock.patch("main.check_instrument_has_daybatch") as mock_check_instrument_has_daybatch:
            mock_check_instrument_has_daybatch.return_value = False
            with mock.patch("main.create_daybatch_for_instrument") as mock_create_daybatch_for_instrument:
                mock_create_daybatch_for_instrument.side_effect = mock_create_daybatch(context)
                create_daybatches(None, None)


@given("'{instrument_name}' is installed")
def step_impl(context, instrument_name):
    if not hasattr(context, "installed_instrument_data"):
        context.installed_instrument_data = {}
    mock_installed_instrument_data = deepcopy(mock_installed_instrument_data_template)
    mock_installed_instrument_data["name"] = instrument_name
    context.installed_instrument_data[instrument_name] = mock_installed_instrument_data


@given("'{instrument_name}' has an active survey day of today")
def step_impl(context, instrument_name):
    context.installed_instrument_data[instrument_name]
    installed_instrument_data = context.installed_instrument_data[instrument_name]
    installed_instrument_data["activeToday"] = True
    context.installed_instrument_data[instrument_name] = installed_instrument_data


@given("'{instrument_name}' has cases")
def step_impl(context, instrument_name):
    installed_instrument_data = context.installed_instrument_data[instrument_name]
    installed_instrument_data["dataRecordCount"] = 100
    context.installed_instrument_data[instrument_name] = installed_instrument_data


@given("'{instrument_name}' does not have an active survey day of today")
def step_impl(context, instrument_name):
    context.installed_instrument_data[instrument_name]
    installed_instrument_data = context.installed_instrument_data[instrument_name]
    installed_instrument_data["activeToday"] = False
    context.installed_instrument_data[instrument_name] = installed_instrument_data


@given("'{instrument_name}' does not have cases")
def step_impl(context, instrument_name):
    installed_instrument_data = context.installed_instrument_data[instrument_name]
    installed_instrument_data["dataRecordCount"] = 0
    context.installed_instrument_data[instrument_name] = installed_instrument_data


@then("no daybatches are created")
def step_impl(context):
    assert len(context.created_daybatches) == 0


@then("a daybatch is created for '{instrument_name}'")
def step_impl(context, instrument_name):
    assert context.created_daybatches.get(instrument_name, 0) > 0, \
        f"context.created_daybatches - {context.created_daybatches}"


@then("a daybatch is not created for '{instrument_name}'")
def step_impl(context, instrument_name):
    assert context.created_daybatches.get(instrument_name, 0) == 0, \
        f"context.created_daybatches - {context.created_daybatches}"
