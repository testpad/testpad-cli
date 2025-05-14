import click

from .base_group import cli
from .config import get_client
from .renderers import PrettyRenderer


@cli.group()
def run():
    pass


@run.command(name="get")
@click.argument("script-id", type=int)
@click.argument("run-id", type=int)
def get_run(script_id: int, run_id: int):
    run_obj = get_client().get_run(script_id, run_id)
    click.echo(PrettyRenderer().render_run(run_obj))
