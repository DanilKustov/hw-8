from main import my_func


def test1(a, b):
    value = my_func(a, b)
    assert value > 0


test1(1, 5)
test1(1, 1)
test1(1, 10)