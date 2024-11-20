from .entrypoint import cli


@cli.command()
def whoami():
    print("yo")
