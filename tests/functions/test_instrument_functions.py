import requests

from functions.instrument_functions import (
    get_installed_instrument_data,
    get_instruments_with_active_survey_day_today_and_cases,
    check_instrument_has_daybatch,
    create_daybatch_for_instrument,
)


def test_get_installed_instrument_data(
    requests_mock, mock_config, mock_installed_instrument_data
):
    requests_mock.get(
        f"http://blah/api/v1/cati/serverparks/blah/instruments",
        json=mock_installed_instrument_data,
    )
    assert get_installed_instrument_data(mock_config) == mock_installed_instrument_data


def test_get_instruments_with_active_survey_day_today_and_cases_returns_only_instruments_with_active_survey_day_today_and_cases(
    mock_installed_instrument_data,
):
    assert get_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data
    ) == ["DST2106X", "DST2106Y"]


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_instruments_have_an_active_survey_day_today(
    mock_installed_instrument_data_with_no_active_survey_day_today,
):
    assert (
        get_instruments_with_active_survey_day_today_and_cases(
            mock_installed_instrument_data_with_no_active_survey_day_today
        )
        == []
    )


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_instruments_have_cases(
    mock_installed_instrument_data_with_no_cases,
):
    assert (
        get_instruments_with_active_survey_day_today_and_cases(
            mock_installed_instrument_data_with_no_cases
        )
        == []
    )


def test_create_daybatch_for_instrument_when_success(requests_mock, mock_config):
    requests_mock.post(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch",
        status_code=201,
    )
    assert create_daybatch_for_instrument(mock_config, "DST2106Z") == "Success"


def test_create_daybatch_for_instrument_when_failure(requests_mock, mock_config):
    requests_mock.post(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch",
        status_code=500,
    )
    assert create_daybatch_for_instrument(mock_config, "DST2106Z") == "Failure"


def test_check_instrument_has_daybatch_when_true(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch/today",
        json=True,
    )
    assert check_instrument_has_daybatch(mock_config, "DST2106Z") is True


def test_check_instrument_has_daybatch_when_false(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch/today",
        json=False,
    )
    assert check_instrument_has_daybatch(mock_config, "DST2106Z") is False


def test_check_instrument_has_daybatch_when_failure(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch/today",
        exc=requests.exceptions.ConnectTimeout,
    )
    assert check_instrument_has_daybatch(mock_config, "DST2106Z") is False


def test_check_instrument_has_daybatch_when_rest_api_failure(
    requests_mock, mock_config
):
    requests_mock.get(
        f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Z/daybatch/today",
        status_code=500,
    )
    assert check_instrument_has_daybatch(mock_config, "DST2106Z") is False
