def find_unique(elements: list) -> list:
    result = []
    for item in elements:
        if elements.count(item) == 1:
            result.append(item)
    return result

