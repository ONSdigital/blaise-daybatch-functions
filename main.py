import os

from dotenv import load_dotenv

from functions.instrument_functions import get_installed_instrument_data, \
    get_instruments_with_active_survey_day_today_and_cases, \
    create_daybatch_for_instrument, check_instrument_has_daybatch
from models.config_model import Config


def create_daybatches(_event, _context):
    print(f"Running Cloud Function - create_daybatches")
    config = Config.from_env()
    config.log()
    installed_instrument_data = get_installed_instrument_data(config)
    if not installed_instrument_data:
        print(f"No instruments installed")
        return
    instruments_with_active_survey_day_today_and_cases = get_instruments_with_active_survey_day_today_and_cases(
        installed_instrument_data)
    if not instruments_with_active_survey_day_today_and_cases:
        print(f"No instruments installed with an active survey day of today and has cases")
        return
    for instrument in instruments_with_active_survey_day_today_and_cases:
        if not check_instrument_has_daybatch(config, instrument):
            create_daybatch_for_instrument(config, instrument)
        else:
            print(f"Instrument {instrument} already has a daybatch for today")


def check_daybatches(_event, _context):
    print("Running Cloud Function - check_daybatches")
    config = Config.from_env()
    config.log()
    installed_instrument_data = get_installed_instrument_data(config)
    if not installed_instrument_data:
        print("No instruments installed")
        return
    instruments_with_active_survey_day_today_and_cases = get_instruments_with_active_survey_day_today_and_cases(
        installed_instrument_data)
    if not instruments_with_active_survey_day_today_and_cases:
        print(f"No instruments installed with an active survey day of today and has cases")
        return
    for instrument in instruments_with_active_survey_day_today_and_cases:
        if not check_instrument_has_daybatch(config, instrument):
            # todo - add email alert
            pass


if os.path.isfile("./.env"):
    print("Loading environment variables from dotenv file")
    load_dotenv()
