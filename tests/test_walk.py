from ast import parse
from sys import version_info
from textwrap import dedent


from flake8_os_walk import OsWalkVisitor


def test_os_walk_func_bad_usage():
    tree = parse(
        dedent(
            """\
        import os

        def hello_jerry():
          for dir in os.walk('this-is-bad'):
            print(dir)
    """
        )
    )
    visitor = OsWalkVisitor()
    visitor.visit(tree)
    violations = visitor.violations
    assert len(violations) == 1

    assert (
        violations[0][1] == "OW100 usage of os.walk() without an onerror param detected"
    )
    node = violations[0][0]
    assert node.lineno == 4
    assert node.col_offset == 13


def test_os_walk_func_onerror_none():
    tree = parse(
        dedent(
            """\
        import os

        def hello_jerry():
          for dir in os.walk('this-is-bad', onerror=None):
            print(dir)
    """
        )
    )
    visitor = OsWalkVisitor()
    visitor.visit(tree)
    violations = visitor.violations
    assert len(violations) == 1

    assert (
        violations[0][1] == "OW100 usage of os.walk() without an onerror param detected"
    )
    node = violations[0][0]
    assert node.lineno == 4
    assert node.col_offset == 13


def test_os_walk_func():
    tree = parse(
        dedent(
            """\
        import os

        def _handle_error(error):
            raise Exception("no soup for you.")

        def hello_jerry():
          for dir in os.walk('this-is-bad', onerror=_handle_error):
            print(dir)
    """
        )
    )
    visitor = OsWalkVisitor()
    visitor.visit(tree)
    assert len(visitor.violations) == 0


def test_os_walk_method_bad_usage():
    tree = parse(
        dedent(
            """\
        import os

        class Festivus:
            def tinsel(self):
                for dir in os.walk('this-is-bad'):
                    print(dir)
    """
        )
    )
    visitor = OsWalkVisitor()
    visitor.visit(tree)
    violations = visitor.violations
    assert len(violations) == 1

    assert (
        violations[0][1] == "OW100 usage of os.walk() without an onerror param detected"
    )
    node = violations[0][0]
    assert node.lineno == 5
    assert node.col_offset == 19
