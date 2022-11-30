import astroid
from astroid import nodes
from typing import TYPE_CHECKING

from pylint.checkers import BaseChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class NotOddChecker(BaseChecker):

    name = "not-odd"
    msgs = {
        "W0001": (
            "Odd numbers are not allowed",
            "not-odd",
            "All numbers should be even.",
        ),
    }

    def visit_assign(self, node):
        if isinstance(node.value, nodes.Const):
            if node.value.value % 2 == 1:
                self.add_message("not-odd", node=node)
        elif isinstance(node.value, nodes.Call):
            for infered in node.value.infer():
                if isinstance(infered, nodes.Const):
                    if infered.value % 2 == 1:
                        self.add_message("not-odd", node=node)

def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.
    :param linter: The linter to register the checker to.
    """
    linter.register_checker(NotOddChecker(linter))
