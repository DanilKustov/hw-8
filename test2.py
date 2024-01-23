from main import my_func


def test2(a, b):
    result = my_func(a, b)
    assert result == 0


test2(2, 2)
test2(1, 1)
test2(10, 10)
