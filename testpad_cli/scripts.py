# from .base_group import cli
# import click
#
# from .config import get_client
#
#
# @cli.group()
# def script():
#     pass
#
#
# @script.command()
# @click.argument("project-id", type=int)
# @click.argument("script-id", type=int)
# def get_script(project_id: int, script_id: int):
#     script = get_client().get(project_id, script_id)
#
