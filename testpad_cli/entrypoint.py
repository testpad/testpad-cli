from .base_group import cli
from .projects import *

# these are needed to make click realise that there are sub-commands
# flake8:noqa
# noqa
from .utils import *

if __name__ == "__main__":
    cli()
