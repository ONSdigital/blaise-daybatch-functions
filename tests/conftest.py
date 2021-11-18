import pytest

from models.config_model import Config


@pytest.fixture
def mock_config():
    return Config(
        blaise_server_park="blah",
        blaise_api_url="blah"
    )


@pytest.fixture
def mock_installed_instrument_data():
    return [
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Y",
            "id": "12345-12345-12345-12345-YYYYY",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 42,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Z",
            "id": "12345-12345-12345-12345-ZZZZZ",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 0,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        }
    ]


@pytest.fixture
def mock_installed_instrument_data_with_no_active_survey_day_today():
    return [
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": False,
            "dataRecordCount": 1337,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Y",
            "id": "12345-12345-12345-12345-YYYYY",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": False,
            "dataRecordCount": 42,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Z",
            "id": "12345-12345-12345-12345-ZZZZZ",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": False,
            "dataRecordCount": 0,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        }
    ]


@pytest.fixture
def mock_installed_instrument_data_with_no_cases():
    return [
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106X",
            "id": "12345-12345-12345-12345-XXXXX",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 0,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Y",
            "id": "12345-12345-12345-12345-YYYYY",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 0,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        },
        {
            "surveyDays": [
                "2021-01-01T01:01:01.999Z"
            ],
            "name": "DST2106Z",
            "id": "12345-12345-12345-12345-ZZZZZ",
            "serverParkName": "gusty",
            "installDate": "2021-01-01T01:01:01.999Z",
            "status": "Active",
            "activeToday": True,
            "dataRecordCount": 0,
            "hasData": True,
            "nodes": [
                {
                    "nodeName": "blaise-gusty-mgmt",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-1",
                    "nodeStatus": "Active"
                },
                {
                    "nodeName": "blaise-gusty-data-entry-2",
                    "nodeStatus": "Active"
                }
            ]
        }
    ]
