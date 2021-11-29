from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        str_res = 'Позиционные аргументы: \n'
        if len(args) > 0:
            for i in range(0, len(args)):
                str_res = str_res + (f'{func.__name__} ({args[i]}, {type(args[i])})') + ', '
        else:
                str_res = str_res + 'Не введены!  \n'
        str_res = str_res + '\nИменнованные аргументы: \n'
        if len(kwargs) > 0:
            #str_res = str_res[:(len(str_res) - 2)]
            for key, val in kwargs.items():
                str_res = str_res + (f'{func.__name__} ({val}, {type(val)})') + ', '
        else:
                str_res = str_res + 'Не введены!  '
        return str_res[:(len(str_res) - 2)]

    return wrapper

@type_logger
def calc_cube(*args, **kwargs):
    """Функция возвращает куб числа."""
    list_result = []
    if len(args) > 0:
        for elem in args:
            list_result.append(elem ** 3)
    if len(kwargs) > 0:
        for key,val in kwargs.items():
            list_result.append(val ** 3)
    return list_result

str_result = calc_cube(6, 5, 9, 8, a = 6, b = 7)
print(str_result)
print('')
print(calc_cube.__doc__)  # Проверяем "маскировку" функции.
