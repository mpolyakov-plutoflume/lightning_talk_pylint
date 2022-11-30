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
        self.add_message("not-odd", node=node)

def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.
    :param linter: The linter to register the checker to.
    """
    linter.register_checker(NotOddChecker(linter))
