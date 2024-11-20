from .base_group import cli


@cli.group()
def project():
    pass


@project.command(name="ls")
def list_projects():
    print("lala")
