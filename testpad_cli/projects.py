import sys

import click
from tabulate import tabulate
from testpad.exceptions import NotFound

from .base_group import cli
from .config import get_client
from .renderers import PrettyRenderer


@cli.group()
def project():
    pass


@project.command(name="ls")
def list_projects():
    header = ["Id", "Name", "Description"]
    rows = [
        (proj.id, proj.name, proj.description) for proj in get_client().list_projects()
    ]
    click.echo(tabulate(rows, headers=header))


@project.command(name="get")
@click.argument("project-id", type=int)
def get_project(project_id):
    client = get_client()

    try:
        proj_obj = client.get_project(project_id)
    except NotFound:
        error = click.style(
            f"Project with ID {project_id} does not exist or you are not allowed to see it",
            fg="red",
        )
        click.echo(error, err=True)
        sys.exit(1)

    click.echo(click.style(proj_obj.name, bold=True, underline=True))
    click.echo(f"{proj_obj.description}\n")

    contents = client.get_project_contents(project_id)
    click.echo(PrettyRenderer().render_contents(contents))
