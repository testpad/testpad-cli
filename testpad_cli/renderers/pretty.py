import click
from testpad.models import Folder, Note, Script

from ._base import BaseRenderer


class PrettyRenderer(BaseRenderer):

    def render_note(self, note: Note) -> str:
        return click.style(f":: {note.name} ::", fg="white")

    def render_script(self, script: Script) -> str:
        rendered = script.name
        if script.description:
            rendered = f"{rendered}\n\t{script.description}"
        return click.style(rendered, fg="green")

    def render_folder(self, folder: Folder, indent: int = 0) -> str:
        rendered = "" if folder.name == "root" else folder.name
        rendered = click.style(rendered, fg="red")

        tabs = "\t" * indent
        for obj in folder.contents:
            if obj.type == "script":
                obj_str = self.render_script(obj)
            elif obj.type == "note":
                obj_str = self.render_note(obj)
            elif obj.type == "folder":
                obj_str = self.render_folder(obj, indent + 1)
            else:
                raise ValueError(f"Cannot render object of type {obj.type}")
            rendered += f"\n{tabs}{obj_str}"
        return rendered
