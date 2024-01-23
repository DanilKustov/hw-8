from main import my_func


def test1(a, b):
    value = my_func(a, b)
    assert value > 0


test1(1, 5)
test1(1, 7)
test1(3, 10)