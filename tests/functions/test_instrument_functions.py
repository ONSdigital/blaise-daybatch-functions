from functions.instrument_functions import get_installed_instrument_data, \
    get_instruments_with_active_survey_day_today_and_cases, check_instrument_has_daybatch


def test_get_installed_instrument_data(requests_mock, mock_config, mock_installed_instrument_data):
    requests_mock.get(f"http://blah/api/v1/cati/serverparks/blah/instruments", json=mock_installed_instrument_data)
    assert get_installed_instrument_data(mock_config) == mock_installed_instrument_data


def test_get_instruments_with_active_survey_day_today_and_cases_returns_only_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data):
    assert get_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data) == ['DST2106X', 'DST2106Y']


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_instruments_have_an_active_survey_day_today(
        mock_installed_instrument_data_with_no_active_survey_day_today):
    assert get_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data_with_no_active_survey_day_today) == []


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_instruments_have_cases(
        mock_installed_instrument_data_with_no_cases):
    assert get_instruments_with_active_survey_day_today_and_cases(mock_installed_instrument_data_with_no_cases) == []


def test_check_instrument_has_daybatch_when_true(requests_mock, mock_config):
    requests_mock.get(f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106X/daybatch", status_code=200)
    assert check_instrument_has_daybatch(mock_config, "DST2106X") is True


def test_check_instrument_has_daybatch_when_false(requests_mock, mock_config):
    requests_mock.get(f"http://blah/api/v1/cati/serverparks/blah/instruments/DST2106Y/daybatch", status_code=500)
    assert check_instrument_has_daybatch(mock_config, "DST2106Y") is False
