import asyncio
from unittest.mock import patch

import requests

from functions.questionnaire_functions import (
    get_installed_questionnaire_data,
    get_questionnaires_with_active_survey_day_today_and_cases,
    check_questionnaire_has_daybatch,
    create_daybatch_for_questionnaire,
    create_daybatch_for_questionnaire_async,
)


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


@patch.object(asyncio, "ensure_future")
def test_create_create_daybatch_for_questionnaire_passes_correct_arguments_to_asyncio(
        mock_asyncio, mock_config):
    # arrange

    # act
    create_daybatch_for_questionnaire(mock_config, "DST2106Z")

    # assert
    assert mock_asyncio.called_once()


async def test_create_daybatch_for_questionnaire_async_returns_success(requests_mock, mock_config):
    # arrange
    requests_mock.post(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch",
        status_code=201,
    )

    # act
    result = await create_daybatch_for_questionnaire_async(mock_config, "DST2106Z")

    # assert
    assert result == "Success"


async def test_create_daybatch_for_questionnaire_async_returns_failure_when_api_fails(requests_mock, mock_config):
    # arrange
    requests_mock.post(
        f"http://blah/api/v2/cati/serverparks/blah/questionnaires/DST2106Z/daybatch",
        status_code=500,
    )

    # act
    result = await create_daybatch_for_questionnaire_async(mock_config, "DST2106Z")

    # assert
    assert result == "Failure"


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
