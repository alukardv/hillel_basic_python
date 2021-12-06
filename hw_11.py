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
