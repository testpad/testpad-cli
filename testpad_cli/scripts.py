import click

from .base_group import cli
from .config import get_client
from .renderers import PrettyRenderer


@cli.group()
def script():
    pass


@script.command(name="get")
@click.argument("script-id", type=int)
def get_script(script_id: int):
    script = get_client().get_script(script_id)
    click.echo(PrettyRenderer().render_script(script))
