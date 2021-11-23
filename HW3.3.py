# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


arg1 = int(input("input arg1"))
arg2 = int(input("input arg2"))
arg3 = int(input("input arg3"))

def my_func(arg1, arg2, arg3):
    if arg2 > arg1 and arg3 > arg1:
        return arg2 + arg3
    elif arg1 > arg2 and arg3 > arg2:
        return arg1 + arg3
    else: return arg1 + arg2


print(f'result {my_func(arg1, arg2, arg3)}')