from testpad.models import Folder, Note, Script

from ._base import BaseRenderer


class JsonRenderer(BaseRenderer):
    def render_script(self, script: Script) -> str:
        pass

    def render_contents(self, folder: Folder) -> str:
        pass

    def render_note(self, note: Note) -> str:
        pass
