"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide
from click.testing import CliRunner
from main import add_cli


# write a test for the add_cli function that calls the add_cli function with the arguments 1 and 2 and checks that the output is 3.
def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert subtract(10, 2) == 8

def test_mult():
    assert multiply(3, 3) == 9

def test_div():
    assert divide(20, 10) == 2


def test_help():
    """Tests the command-line interface help message."""
    runner = CliRunner()
    result = runner.invoke(add_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output



