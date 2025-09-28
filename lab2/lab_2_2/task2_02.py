# 2) Слияние

# Напишите функцию, которая производит слияние двух словарей. Используйте рекурсию.
# В обоих словарях может быть любой уровень вложенности.
# Вложены могут быть другие коллекции: словари, списки, множества, кортежи.
# Пример:
# >> dict_a = {“a”: 1, “b”: {“c”: 1, “f”: 4}}
# >> dict_b = {“d”: 1, “b”: {“c”: 2, “e”: 3}}
# >> merge_dicts(dict_a, dict_b)
# >> print(dict_a)
# {“a”: 1, “b”: {“c”: 2, “e”: 3, “f”: 4}, “d”: 1}

def merge(a, b):
    for key in b:
        if key in a:
            # оба словари - рекурсивно объединяет
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key])
            # оба списки - объединяет без повторов
            elif isinstance(a[key], list) and isinstance(b[key], list):
                merge(a[key], b[key])
            # оба множества - объединяет
            elif isinstance(a[key], set) and isinstance(b[key], set):
                merge(a[key], b[key])
            # оба кортежи - объединяет и превращвет в кортеж
            elif isinstance(a[key], tuple) and isinstance(b[key], tuple):
                merge(a[key], b[key])
            else:
               a[key] = b[key]
        else:
            a[key] = b[key] # в a нет ключа - добавить

dict_a = {"a": 1, "b":{"c": 1, "f": 4}}
dict_b = {"d": 1, "b":{"c": 2, "e": 3}}

merge(dict_a, dict_b)
print(dict_a)