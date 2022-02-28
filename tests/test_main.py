from unittest.mock import patch

from main import create_daybatches, check_daybatches


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
    assert create_daybatches(None, None) == "No instruments installed"
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
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = []
    assert create_daybatches(None, None) == "No instruments installed with an active survey day of today and has cases"
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
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = []
    assert create_daybatches(None, None) == "No instruments installed with an active survey day of today and has cases"
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
    assert create_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_create_daybatch_for_instrument.call_count == 2


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_two_instruments_are_valid_but_one_fails_on_daybatch_check_still_creates_a_daybatch_for_the_other_instrument(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.side_effect = [Exception('Whooopsy!'), False]
    assert create_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_create_daybatch_for_instrument.call_count == 1


@patch("main.create_daybatch_for_instrument")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_create_daybatches_when_two_instruments_are_valid_but_one_fails_on_daybatch_creation_still_creates_a_daybatch_for_the_other_instrument(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_create_daybatch_for_instrument,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.return_value = False
    mock_create_daybatch_for_instrument.side_effect = [Exception('Whooopsy!'), "Success"]
    assert create_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_create_daybatch_for_instrument.call_count == 2    


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_when_no_instruments_installed(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch):
    mock_get_installed_instrument_data.return_value = []
    assert check_daybatches(None, None) == "No instruments installed"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 0
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 0


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_when_instruments_installed_but_no_active_survey_day_today(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch,
        mock_installed_instrument_data_with_no_active_survey_day_today):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data_with_no_active_survey_day_today
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = []
    assert check_daybatches(None, None) == "No instruments installed with an active survey day of today and has cases"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 0


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_when_instruments_installed_but_no_cases(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch,
        mock_installed_instrument_data_with_no_cases):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data_with_no_cases
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = []
    assert check_daybatches(None, None) == "No instruments installed with an active survey day of today and has cases"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 0
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 0


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_when_two_out_of_three_instruments_are_valid_for_daybatch_checking_but_dont_have_daybatches(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.return_value = False
    assert check_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 2


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_sends_email_for_other_instrument_when_previous_daybatch_check_fails(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.side_effect = [Exception('Whooopsy!'), False]
    assert check_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 1    


@patch("main.send_email_notification_for_instrument_without_daybatch")
@patch("main.check_instrument_has_daybatch")
@patch("main.get_instruments_with_active_survey_day_today_and_cases")
@patch("main.get_installed_instrument_data")
def test_check_daybatches_sends_email_for_other_instrument_when_previous_email_fails(
        mock_get_installed_instrument_data,
        mock_get_instruments_with_active_survey_day_today_and_cases,
        mock_check_instrument_has_daybatch,
        mock_send_email_notification_for_instrument_without_daybatch,
        mock_installed_instrument_data):
    mock_get_installed_instrument_data.return_value = mock_installed_instrument_data
    mock_get_instruments_with_active_survey_day_today_and_cases.return_value = ['DST2106X', 'DST2106Y']
    mock_check_instrument_has_daybatch.return_value = False
    mock_send_email_notification_for_instrument_without_daybatch.side_effect = [Exception('Whooopsy!'), False]
    assert check_daybatches(None, None) == "Finished"
    assert mock_get_installed_instrument_data.call_count == 1
    assert mock_get_instruments_with_active_survey_day_today_and_cases.call_count == 1
    assert mock_check_instrument_has_daybatch.call_count == 2
    assert mock_send_email_notification_for_instrument_without_daybatch.call_count == 2        
