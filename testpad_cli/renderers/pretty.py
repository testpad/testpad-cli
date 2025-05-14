from typing import List, Union

import click
from testpad.models import Folder, Note, Run, Script, Test, TestResult

from ._base import BaseRenderer


class PrettyRenderer(BaseRenderer):

    def render_test_result(self, result: TestResult) -> str:
        if result.passed:
            rendered = click.style("Pass", fg="green")
        else:
            rendered = click.style("Fail", fg="red")
        if result.comment:
            rendered += f"\n - {result.comment}"
        return rendered

    def render_run(self, run: Run) -> str:
        rendered = ""
        for case, result in run.results.items():
            rendered += f"{case:3s}: {self.render_test_result(result)}\n"
        return rendered

    def render_note(self, note: Note) -> str:
        return click.style(f":: {note.name} ::", fg="white")

    def render_test(self, test: Test) -> str:
        indent = "   " * test.indent
        number = click.style(f"{test.id:4d}", fg="yellow")
        rendered = f"{number} :: {indent}{test.text}"
        return rendered

    def render_script(self, script: Script) -> str:
        rendered = script.name
        if script.description:
            rendered = f"{rendered}\n\t{script.description}"
        tests = (
            [self.render_test(test) for test in script.tests] if script.tests else []
        )
        rendered += "\n\n" + "\n".join(tests)
        return rendered

    def render_contents(
        self, contents: List[Union[Note, Script, Folder]], indent: int = 0
    ) -> str:
        # rendered = "" if folder.name == "root" else folder.name
        # rendered = click.style(rendered, fg="red")
        rendered = ""

        tabs = "\t" * indent
        for obj in contents:
            if obj.type == "script":
                obj_str = self.render_script(obj)
            elif obj.type == "note":
                obj_str = self.render_note(obj)
            elif obj.type == "folder":
                obj_str = self.render_contents(obj.contents, indent + 1)
            else:
                raise ValueError(f"Cannot render object of type {obj.type}")
            rendered += f"\n{tabs}{obj_str}"
        return rendered
