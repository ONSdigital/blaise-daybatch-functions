import requests


def api_call():
    return requests.get(f"/api/v1/cati/instruments")
