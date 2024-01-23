def my_func(a, b):
    result = 0
    if a < b:
        for i in range(b-a):
            result += i
    else:
        for i in range(a-b):
            result += i
    return result


print(my_func(1, 1))