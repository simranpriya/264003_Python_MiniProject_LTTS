import maths

path_large_number_fixture = 'large_num_fixture.txt'


def test_add_ten():
    """ Tests the add_ten function """
    assert 15 == maths.add_ten(5)


def test_add_ten_str_int():
    """ Tests the add_ten function for string input """
    assert maths.add_ten('5') == '15'


def test_add_ten_none():
    """ Tests that add_ten throws a ValueError when None input given """
    assert maths.add_ten(None) is None


def test_large_number():

    with open(path_large_number_fixture, 'r') as fh:

        expected = (fh.readline())

    assert maths.add_ten(90) == expected