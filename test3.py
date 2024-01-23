from main import my_func


def test3(a, b):
    result = a + b
    assert result == "string"


test3(1, 5)
test3(1, 1)
test3(1, 10)
