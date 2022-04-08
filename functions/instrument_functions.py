from datetime import datetime

import requests


def get_installed_instrument_data(config):
    print(f"Getting instrument data")
    try:
        response = requests.get(
            f"http://{config.blaise_api_url}/api/v1/cati/serverparks/{config.blaise_server_park}/instruments"
        )
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print(f"Error when getting installed instrument data via the API - ", error)


def get_instruments_with_active_survey_day_today_and_cases(installed_instrument_data):
    print(f"Getting instruments with an active survey day of today and has cases")
    active_survey_day_instruments = []
    for instrument in installed_instrument_data:
        if instrument["activeToday"] and instrument["dataRecordCount"] > 0:
            active_survey_day_instruments.append(instrument["name"])
    return active_survey_day_instruments


def create_daybatch_for_instrument(config, instrument):
    print(f"Creating daybatch for instrument {instrument}")
    today = datetime.now()
    post_data = {"dayBatchDate": str(today), "checkForTreatedCases": True}
    try:
        response = requests.post(
            f"http://{config.blaise_api_url}/api/v1/cati/serverparks/{config.blaise_server_park}/instruments/{instrument}/daybatch",
            json=post_data,
        )
        if response.status_code == 201:
            print(f"Daybatch successfully created for {instrument}")
            return "Success"
        else:
            print(
                f"Failure when creating daybatch for instrument {instrument} via the API - ",
                response.status_code,
            )
            return "Failure"
    except requests.exceptions.RequestException as error:
        print(
            f"Error when creating daybatch for instrument {instrument} via the API - ",
            error,
        )


def check_instrument_has_daybatch(config, instrument):
    print(f"Checking if instrument {instrument} has a daybatch for today")
    try:
        response = requests.get(
            f"http://{config.blaise_api_url}/api/v1/cati/serverparks/{config.blaise_server_park}/instruments/{instrument}/daybatch/today"
        )
        if response.status_code == 200 and response.json():
            print(f"Instrument {instrument} has a daybatch for today")
            return True
        else:
            print(f"Instrument {instrument} does not have a daybatch for today")
            return False
    except requests.exceptions.RequestException as error:
        print(
            f"Error when checking if instrument {instrument} has a daybatch for today via the API - ",
            error,
        )
        return False
