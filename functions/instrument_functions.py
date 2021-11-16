import time
from datetime import datetime

import requests


def get_installed_instrument_data(config):
    print(f"Getting instrument data")
    try:
        response = requests.get(
            f"http://{config.blaise_api_url}/api/v1/cati/serverparks/{config.blaise_server_park}/instruments")
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print(f"Error when getting instrument data via the API - ", error)


def get_active_survey_day_instruments(installed_instrument_data):
    print(f"Getting active survey day instruments")
    active_survey_day_instruments = []
    for instrument in installed_instrument_data:
        if instrument['activeToday']:
            active_survey_day_instruments.append(instrument['name'])
    return active_survey_day_instruments


def create_daybatch_for_instrument(config, instrument):
    print(f"Creating daybatch for instrument {instrument}")
    today = datetime.now()
    post_data = {"dayBatchDate": str(today), "checkForTreatedCases": True}
    for attempt in range(3):
        try:
            response = requests.post(
                f"http://{config.blaise_api_url}/api/v1/cati/serverparks/{config.blaise_server_park}/instruments/{instrument}/daybatch",
                json=post_data)
            if response.status_code == 201:
                print(f"Daybatch successfully created for {instrument}")
                return
            else:
                print(f"Failure when creating daybatch for instrument {instrument} via the API - ",
                      response.status_code)
            if attempt != 2:
                time.sleep(300)
        except requests.exceptions.RequestException as error:
            print(f"Error when creating daybatch for instrument {instrument} via the API - ", error)
