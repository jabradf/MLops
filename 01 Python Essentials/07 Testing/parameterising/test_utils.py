# run `pytest` in terminal, no extra filenames needed.
import pytest
from utils import str_to_bool


'''
def test_yes_is_true():
    # don't be tempted to wrap the tests inside a loop, as the fail won't show which failure it stopped at.
    result = str_to_bool('yes')
    assert result is True


def test_y_is_true():
    result = str_to_bool('y')
    assert result is True
    '''


# use a decorator to add extra functionality. 
# This string of values is a good way to run all tests
# It will output each permutation and the exact test that it failed at, and also continue on.
@pytest.mark.parametrize('value', ['y', 'n', 'yes', ''])
def test_is_true(value):
    result = str_to_bool(value)
    assert result is True
