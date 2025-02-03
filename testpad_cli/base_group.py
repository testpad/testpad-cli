import sys

import click

from .config import TOKEN_ENVIRONMENT_NAME, get_client
from .exceptions import TokenNotProvided


@click.group
def cli():
    try:
        # sanity check before running anything
        get_client()
    except TokenNotProvided:
        msg = click.style(
            f"You must provide your TestPad API token. Set the {TOKEN_ENVIRONMENT_NAME} environment variable.",
            fg="red",
            bold=True,
        )
        click.echo(msg, err=True, color=True)
        sys.exit(1)
