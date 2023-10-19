
# This function is here for convenience only, in a real-world scenario this function
# would be elsewhere in a package

def str_to_int(string):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    You can pass "1.1" which returns 1
    ["1"] -> raises RuntimeError
    """
    error_msg = "Unable to convert to integer: '%s'" % str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        # this might be a integer already, so try to use it, otherwise raise
        # the original exception
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        raise RuntimeError(error_msg)

    return int(integer)


class TestStrToInt:

    def setup(self):
        print('\nthis is setup')    # run before every test in the class

    def teardown(self):
        print('\nthis is teardown') # runs after every test in the class, regardless of pass/fail status

    def setup_class(cls):
        print('\nthis is setup class')  # run once before the tests in the class

    def teardown_class(cls):
        print('\nthis is teardown class')   # run once after tests in class

    def test_rounds_down(self):
        result = str_to_int('1.99')
        assert result == 2

    def test_round_down_lesser_half(self):
        result = str_to_int('1.2')
        assert result == 2
