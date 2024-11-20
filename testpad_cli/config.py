import os

from .exceptions import TokenNotProvided

TOKEN_ENVIRONMENT_NAME = "TESTPAD_TOKEN"


def get_token() -> str:
    token = os.environ.get(TOKEN_ENVIRONMENT_NAME)
    if token is not None:
        return token
    raise TokenNotProvided
