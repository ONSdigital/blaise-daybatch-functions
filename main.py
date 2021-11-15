import os

from dotenv import load_dotenv

from functions.instrument_functions import get_installed_instrument_data, get_active_survey_day_instruments, \
    create_daybatch_for_instrument
from models.config_model import Config


def create_daybatches(_event, _context):
    print("Running Cloud Function - create_daybatches")
    config = Config.from_env()
    config.log()
    installed_instrument_data = get_installed_instrument_data(config)
    if not installed_instrument_data:
        print("No instruments installed")
        return
    active_survey_day_instruments = get_active_survey_day_instruments(installed_instrument_data)
    if not active_survey_day_instruments:
        print("No instruments installed with an active survey day today")
        return
    for instrument in active_survey_day_instruments:
        create_daybatch_for_instrument(config, instrument)


def check_daybatches(_event, _context):
    print("Running Cloud Function - check_daybatches")
    config = Config.from_env()
    config.log()
    installed_instrument_data = get_installed_instrument_data(config)
    if not installed_instrument_data:
        print("No instruments installed")
        return
    active_survey_day_instruments = get_active_survey_day_instruments(installed_instrument_data)
    if not active_survey_day_instruments:
        print("No instruments installed with an active survey day today")
        return
    for instrument in active_survey_day_instruments:
        pass


if os.path.isfile("./.env"):
    print("Loading environment variables from dotenv file")
    load_dotenv()
