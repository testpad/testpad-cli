import abc
from typing import List, Union

from testpad.models import Folder, Note, Script


class BaseRenderer(abc.ABC):

    def render_note(self, note: Note) -> str:
        raise NotImplementedError()

    def render_script(self, script: Script) -> str:
        raise NotImplementedError()

    def render_contents(self, contents: List[Union[Script, Note, Folder]]) -> str:
        raise NotImplementedError()
