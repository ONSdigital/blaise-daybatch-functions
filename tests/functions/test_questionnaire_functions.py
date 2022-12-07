import requests

from functions.questionnaire_functions import (
    get_installed_questionnaire_data,
    get_questionnaires_with_active_survey_day_today_and_cases,
    check_questionnaire_has_daybatch,
    create_daybatch_for_questionnaire,
    create_daybatches_concurrently,
    create_daybatch
)

from unittest.mock import patch

def test_get_installed_questionnaire_data(
    requests_mock, mock_config, mock_installed_questionnaire_data
):
    requests_mock.get(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires",
        json=mock_installed_questionnaire_data,
    )
    assert get_installed_questionnaire_data(mock_config) == mock_installed_questionnaire_data


def test_get_questionnaires_with_active_survey_day_today_and_cases_returns_only_questionnaires_with_active_survey_day_today_and_cases(
    mock_installed_questionnaire_data,
):
    assert get_questionnaires_with_active_survey_day_today_and_cases(
        mock_installed_questionnaire_data
    ) == ["DST2106X", "DST2106Y"]


def test_get_questionnaires_with_active_survey_day_today_and_cases_when_no_questionnaires_have_an_active_survey_day_today(
    mock_installed_questionnaire_data_with_no_active_survey_day_today,
):
    assert (
        get_questionnaires_with_active_survey_day_today_and_cases(
            mock_installed_questionnaire_data_with_no_active_survey_day_today
        )
        == []
    )


def test_get_questionnaires_with_active_survey_day_today_and_cases_when_no_questionnaires_have_cases(
    mock_installed_questionnaire_data_with_no_cases,
):
    assert (
        get_questionnaires_with_active_survey_day_today_and_cases(
            mock_installed_questionnaire_data_with_no_cases
        )
        == []
    )


def test_create_daybatch_for_questionnaire_when_success(requests_mock, mock_config):
    requests_mock.post(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch",
        status_code=201,
    )
    assert create_daybatch_for_questionnaire(mock_config, "DST2106Z") == "Success"


def test_create_daybatch_for_questionnaire_when_failure(requests_mock, mock_config):
    requests_mock.post(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch",
        status_code=500,
    )
    assert create_daybatch_for_questionnaire(mock_config, "DST2106Z") == "Failure"


def test_check_questionnaire_has_daybatch_when_true(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch/today",
        json=True,
    )
    assert check_questionnaire_has_daybatch(mock_config, "DST2106Z") is True


def test_check_questionnaire_has_daybatch_when_false(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch/today",
        json=False,
    )
    assert check_questionnaire_has_daybatch(mock_config, "DST2106Z") is False


def test_check_questionnaire_has_daybatch_when_failure(requests_mock, mock_config):
    requests_mock.get(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch/today",
        exc=requests.exceptions.ConnectTimeout,
    )
    assert check_questionnaire_has_daybatch(mock_config, "DST2106Z") is False


def test_check_questionnaire_has_daybatch_when_rest_api_failure(
    requests_mock, mock_config
):
    requests_mock.get(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch/today",
        status_code=500,
    )
    assert check_questionnaire_has_daybatch(mock_config, "DST2106Z") is False
