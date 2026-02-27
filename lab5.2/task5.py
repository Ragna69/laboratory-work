def combine_dicts(dict1: dict, dict2: dict) -> dict:
#Принимает два словаря и делает новый словарь
#содержащий все элементы из обоих, сохраняя порядок
#Если ключи совпадают, значение берётся из второго словаря
    result = {}
    for key, value in dict1.items():    #добавляет элементы первого словаря
        result[key] = value
    for key, value in dict2.items():    #добавляет элементы второго словаря
        result[key] = value
    return result

