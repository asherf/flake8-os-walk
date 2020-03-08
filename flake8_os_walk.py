"""Extension for flake8 that finds usage os.walk()."""
import ast

import pycodestyle
from flake8 import utils as stdin_utils

__version__ = "0.1.0"

ERROR_CODE = "OW100"


class OsWalkVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(OsWalkVisitor, self).__init__(*args, **kwargs)
        self.violations = []

    def visit_Call(self, node):
        self._check_os_walk(node)
        self.generic_visit(node)

    def _check_os_walk(self, node):
        if getattr(node.func, "attr", None) != "walk":
            return
        func_val = getattr(node.func, "value", None)
        if not func_val:
            return
        if getattr(func_val, "id", None) != "os":
            return
        keywords = node.keywords or []
        onerror_keyword = next(
            (keyword for keyword in keywords if keyword.arg == "onerror"), None
        )
        if onerror_keyword:
            value = onerror_keyword.value
            if getattr(value, "value", 0) is not None:
                return
        self.violations.append(
            (
                node,
                "{0} usage of os.walk() without an onerror param detected".format(
                    ERROR_CODE
                ),
            )
        )


class OSWalkChecker(object):
    options = None
    name = "flake8-os-walk"
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename
        self.lines = None

    def load_file(self):
        if self.filename in ("stdin", "-", None):
            self.filename = "stdin"
            self.lines = stdin_utils.stdin_get_value().splitlines(True)
        else:
            self.lines = pycodestyle.readlines(self.filename)

        if not self.tree:
            self.tree = ast.parse("".join(self.lines))

    def run(self):
        if not self.tree or not self.lines:
            self.load_file()

        visitor = OsWalkVisitor()
        visitor.visit(self.tree)
        for node, reason in visitor.violations:
            yield node.lineno, node.col_offset, reason, type(self)
