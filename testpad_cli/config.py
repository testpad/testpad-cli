import os

from testpad import Testpad

from .exceptions import TokenNotProvided

TOKEN_ENVIRONMENT_NAME = "TESTPAD_TOKEN"


def get_client() -> Testpad:
    token = os.environ.get(TOKEN_ENVIRONMENT_NAME)
    if token is None:
        raise TokenNotProvided
    return Testpad(token, api_url=os.environ.get("TESTPAD_API_URL"))
