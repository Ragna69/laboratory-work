# 9) Проверка типов параметров

# Напишите декоратор @type_check, который проверяет, что параметры
# функции соответствуют указанным типам. Если нет - выбрасывает исключение TypeError.
# Пример:
# @type_check(int, int)
# def add(a, b):
# …

def type_check(*expected_types): # принимает типы аргументов
    def decorator(func): # внутренняя функция-декоратор, принимающая саму функцию
        def wrapper(*args, **kwargs):
            for i, (arg, expected) in enumerate(zip(args, expected_types)): # перебираем аргументы и соответствующие типы
                if not isinstance(arg, expected): # если тип аргумента не совпадает с ожидаемым
                    raise TypeError( # выбрасывает исключение с пояснением
                        f"Аргумент #{i + 1} должен быть типа {expected.__name__}, но получен {type(arg).__name__}"
#                                                             expected.__name__ — имя ожидаемого типа (например, 'int')
#                                                             type(arg).__name__ — имя фактического типа (например, 'str')
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(25, 75))
print(add(2, "hello"))

