import abc

from testpad.models import Folder, Note, Script


class BaseRenderer(abc.ABC):

    def render_note(self, note: Note) -> str:
        raise NotImplementedError()

    def render_script(self, script: Script) -> str:
        raise NotImplementedError()

    def render_folder(self, folder: Folder) -> str:
        raise NotImplementedError()
