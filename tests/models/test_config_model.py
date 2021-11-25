import os
from unittest import mock

from models.config_model import Config


def test_config():
    config = Config(
        blaise_server_park="blaise_server_park_mock",
        blaise_api_url="blaise_api_url_mock"
    )
    assert config.blaise_server_park == "blaise_server_park_mock"
    assert config.blaise_api_url == "blaise_api_url_mock"


@mock.patch.dict(
    os.environ,
    {
        "BLAISE_SERVER_PARK": "blaise_server_park_mock",
        "BLAISE_API_URL": "blaise_api_url_mock",
    },
)
def test_config_from_env():
    config = Config.from_env()
    assert config.blaise_server_park == "blaise_server_park_mock"
    assert config.blaise_api_url == "blaise_api_url_mock"
