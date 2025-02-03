import click

from .config import get_client
from .entrypoint import cli


@cli.command()
def whoami():
    company, key = get_client().whoami()
    click.echo(f"Authenticated as {company.name} using key {key.label}")
