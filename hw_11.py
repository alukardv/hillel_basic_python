# Задача 1
# 1 Пример
# def generator_1_example():
#     number: int = 1
#     print('Певый элемент')
#     yield number
#     number += 1
#     print('Второй элемент')
#     yield number
#     number += 1
#     print('Третий элемент')
#     yield number
#
#
# for i in generator_1_example():
#     print(i)

# 2 Пример
# generator_cube = (i**3 for i in range(1, 10))
# while True:
#     try:
#         print(generator_cube.__next__())
#     except StopIteration as e:
#         print(f'{e}')
#         break

# 3 Пример
# with open('hw_11_temp.txt', 'r') as file:
#     err_gen = (st for st in file if 'line' in st)
#     for item in err_gen:
#         print(item)


# Задача 2

from functools import reduce


def square_func(x, y):
    return x * y


def my_reduce(function, value):

    value: iter = iter(value)
    result = next(value)

    for i in value:
        result = function(result, i)
    return result

# Задача 3


def test_my_reduce(function, value):
    assert function(square_func, value) == reduce(square_func, value), 'False'
    return True

print(test_my_reduce(my_reduce, [12, 2, 3, 4]))

#print(reduce(square_func, [12,2,3,4]))
