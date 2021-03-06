import os
from unittest import mock

from models.config_model import Config


def test_config():
    config = Config(
        blaise_server_park="blaise_server_park_mock",
        blaise_api_url="blaise_api_url_mock",
        notify_api_key="notify_api_key_mock",
        to_notify_email="to_notify_email_mock"
    )
    assert config.blaise_server_park == "blaise_server_park_mock"
    assert config.blaise_api_url == "blaise_api_url_mock"
    assert config.notify_api_key == "notify_api_key_mock"
    assert config.to_notify_email == "to_notify_email_mock"


@mock.patch.dict(
    os.environ,
    {
        "BLAISE_SERVER_PARK": "blaise_server_park_mock",
        "BLAISE_API_URL": "blaise_api_url_mock",
        "NOTIFY_API_KEY": "notify_api_key_mock",
        "TO_NOTIFY_EMAIL": "to_notify_email_mock",
    },
)
def test_config_from_env():
    config = Config.from_env()
    assert config.blaise_server_park == "blaise_server_park_mock"
    assert config.blaise_api_url == "blaise_api_url_mock"
    assert config.notify_api_key == "notify_api_key_mock"
    assert config.to_notify_email == "to_notify_email_mock"
