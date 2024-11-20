import sys

import click

from .config import TOKEN_ENVIRONMENT_NAME, get_token
from .exceptions import TokenNotProvided


@click.group
def cli():
    try:
        get_token()
    except TokenNotProvided:
        msg = click.style(
            f"You must provide your TestPad API token. Set the {TOKEN_ENVIRONMENT_NAME} environment variable.",
            fg="red",
            bold=True,
        )
        click.echo(msg, err=True, color=True)
        sys.exit(1)
