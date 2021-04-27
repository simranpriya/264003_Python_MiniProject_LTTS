import maths

path_large_number_fixture = 'large_num_fixture.txt'


def test_add_ten():
    assert 15 == maths.add_ten(5)


def test_add_ten_str_int():
    assert maths.add_ten('5') == '15'


def test_add_ten_none():
    assert maths.add_ten(None) is None

def test_subtract_ten():
    assert 25 == maths.add_ten(15)


def test_subtract_ten_str_int():
    assert maths.add_ten('15') == '25'


def test_subtract_ten_none():
    assert maths.subtract_ten(None) is None


def test_multiply_ten():
    assert 50 == maths.multiply_ten(5)


def test_multiply_ten_str_int():
    assert maths.multiply_ten('5') == '50'


def test_multiply_ten_none():
    assert maths.multiply_ten(None) is None


def test_divide_ten():
    assert 15 == maths.divide_ten(150)


def test_divide_ten_str_int():
    assert maths.divide_ten('150') == '15'


def test_divide_ten_none():
    assert maths.divide_ten(None) is None


def test_large_number():

    with open(path_large_number_fixture, 'r') as fh:

        expected = (fh.readline())

    assert maths.add_ten(90) == expected