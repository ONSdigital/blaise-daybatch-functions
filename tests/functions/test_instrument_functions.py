from functions.instrument_functions import get_installed_instrument_data, \
    get_instruments_with_active_survey_day_today_and_cases


def test_get_installed_instrument_data(requests_mock, mock_config, mock_installed_instrument_data):
    requests_mock.get("http://blah/api/v1/cati/serverparks/blah/instruments", json=mock_installed_instrument_data)
    assert get_installed_instrument_data(mock_config) == mock_installed_instrument_data


def test_get_instruments_with_active_survey_day_today_and_cases(mock_installed_instrument_data):
    assert get_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data) == ['DST2106X', 'DST2106Y']


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_active_survey_day_today(
        mock_installed_instrument_data_with_no_active_survey_day_today):
    assert get_instruments_with_active_survey_day_today_and_cases(
        mock_installed_instrument_data_with_no_active_survey_day_today) == []


def test_get_instruments_with_active_survey_day_today_and_cases_when_no_cases(
        mock_installed_instrument_data_with_no_cases):
    assert get_instruments_with_active_survey_day_today_and_cases(mock_installed_instrument_data_with_no_cases) == []
