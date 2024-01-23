from main import my_func


def test2(a, b):
    if a == b:
        result = 0
    assert result == 0


test2(1, 5)
test2(1, 1)
test2(1, 10)
