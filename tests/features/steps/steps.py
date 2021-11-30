from unittest import mock

from behave import given, then, when, step

from main import create_daybatches

mock_installed_instrument_data = [
    {
        "surveyDays": [
            "2021-01-01T01:01:01.999Z"
        ],
        "name": "DST2106X",
        "id": "12345-12345-12345-12345-XXXXX",
        "serverParkName": "gusty",
        "installDate": "2021-01-01T01:01:01.999Z",
        "status": "Active",
        "activeToday": True,
        "dataRecordCount": 1337,
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
    },
    {
        "surveyDays": [
            "2021-01-01T01:01:01.999Z"
        ],
        "name": "DST2106Y",
        "id": "12345-12345-12345-12345-YYYYY",
        "serverParkName": "gusty",
        "installDate": "2021-01-01T01:01:01.999Z",
        "status": "Active",
        "activeToday": True,
        "dataRecordCount": 42,
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
    },
    {
        "surveyDays": [
            "2021-01-01T01:01:01.999Z"
        ],
        "name": "DST2106Z",
        "id": "12345-12345-12345-12345-ZZZZZ",
        "serverParkName": "gusty",
        "installDate": "2021-01-01T01:01:01.999Z",
        "status": "Active",
        "activeToday": True,
        "dataRecordCount": 0,
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
]


@given("there are no instruments installed")
def step_impl(context):
    with mock.patch("main.get_installed_instrument_data") as mock_get_installed_instrument_data:
        mock_get_installed_instrument_data.return_value = []


@when("the create daybatch process is triggered")
def step_impl(context):
    create_daybatches(None, None)


@then("no daybatches are created")
def step_impl(context):
    with mock.patch(
            "main.get_instruments_with_active_survey_day_today_and_cases") as mock_get_instruments_with_active_survey_day_today_and_cases:
        assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 0


@given("there is an instrument installed")
def step_impl(context):
    with mock.patch("main.get_installed_instrument_data") as mock_get_installed_instrument_data:
        mock_get_installed_instrument_data.return_value = mock_installed_instrument_data


@step("the instrument does not have an active survey day of today")
def step_impl(context):
    pass


@step("the instrument does not have cases")
def step_impl(context):
    pass


@step("the instrument does have an active survey day of today")
def step_impl(context):
    assert mock_installed_instrument_data[0]["activeToday"] is True


@step("the instrument does have cases")
def step_impl(context):
    assert mock_installed_instrument_data[0]["dataRecordCount"] > 0


@then("a daybatch is created for the instrument")
def step_impl(context):
    assert create_daybatches.create_daybatch_for_instrument.call_count > 0
    assert create_daybatches == "Finished"


@given("there are two instruments installed")
def step_impl(context):
    pass


@step("the instrument 'OPN2101X' does not have an active survey day of today and does not have cases")
def step_impl(context):
    pass


@step("the instrument 'OPN2101Y' has an active survey day of today and has cases")
def step_impl(context):
    pass


@then("a daybatch is not created for 'OPN2101X'")
def step_impl(context):
    pass


@step("a daybatch is created for 'OPN2101Y'")
def step_impl(context):
    pass


@step("the instrument 'OPN2101Z' has an active survey day of today and has cases")
def step_impl(context):
    pass


@step("a daybatch is created for 'OPN2101Z'")
def step_impl(context):
    pass
