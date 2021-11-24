from unittest.mock import patch

from main import create_daybatches


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_no_instruments_installed(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument):
    mock_get_installed_instrument_data.return_value = []
    create_daybatches(None, None)
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 0
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_create_daybatch_for_instrument.call_count == 0


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_instruments_installed_but_no_active_survey_day_today(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument,
        mock_installed_instrument_data_with_no_active_survey_day_today):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data_with_no_active_survey_day_today
    create_daybatches(None, None)
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_create_daybatch_for_instrument.call_count == 0


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_instruments_installed_but_no_cases(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument,
        mock_installed_instrument_data_with_no_cases):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data_with_no_cases
    create_daybatches(None, None)
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_create_daybatch_for_instrument.call_count == 0


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_two_out_of_three_instruments_are_valid_for_daybatch_creation(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.return_value = False
    create_daybatches(None, None)
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_create_daybatch_for_instrument.call_count == 2
