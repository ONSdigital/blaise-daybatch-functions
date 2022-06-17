from datetime import datetime

import requests


def get_installed_questionnaire_data(config):
    print(f"Getting questionnaire data")
    try:
        response = requests.get(
            f"http://{config.blaise_api_url}/api/v2/cati/serverparks/{config.blaise_server_park}/questionnaires"
        )
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print(f"Error when getting installed questionnaire data via the API - ", error)


def get_questionnaires_with_active_survey_day_today_and_cases(installed_questionnaire_data):
    print(f"Getting questionnaires with an active survey day of today and has cases")
    active_survey_day_questionnaires = []
    for questionnaire in installed_questionnaire_data:
        if questionnaire["activeToday"] and questionnaire["dataRecordCount"] > 0:
            active_survey_day_questionnaires.append(questionnaire["name"])
    return active_survey_day_questionnaires


def create_daybatch_for_questionnaire(config, questionnaire):
    print(f"Creating daybatch for questionnaire {questionnaire}")
    today = datetime.now()
    post_data = {"dayBatchDate": str(today), "checkForTreatedCases": True}
    try:
        response = requests.post(
            f"http://{config.blaise_api_url}/api/v2/cati/serverparks/{config.blaise_server_park}/questionnaires/{questionnaire}/daybatch",
            json=post_data,
        )
        if response.status_code == 201:
            print(f"Daybatch successfully created for {questionnaire}")
            return "Success"
        else:
            print(
                f"Failure when creating daybatch for questionnaire {questionnaire} via the API - ",
                response.status_code,
            )
            return "Failure"
    except requests.exceptions.RequestException as error:
        print(
            f"Error when creating daybatch for questionnaire {questionnaire} via the API - ",
            error,
        )


def check_questionnaire_has_daybatch(config, questionnaire):
    print(f"Checking if questionnaire {questionnaire} has a daybatch for today")
    try:
        response = requests.get(
            f"http://{config.blaise_api_url}/api/v2/cati/serverparks/{config.blaise_server_park}/questionnaires/{questionnaire}/daybatch/today"
        )
        if response.status_code == 200 and response.json():
            print(f"Questionnaire {questionnaire} has a daybatch for today")
            return True
        else:
            print(f"Questionnaire {questionnaire} does not have a daybatch for today")
            return False
    except requests.exceptions.RequestException as error:
        print(
            f"Error when checking if questionnaire {questionnaire} has a daybatch for today via the API - ",
            error,
        )
        return False
