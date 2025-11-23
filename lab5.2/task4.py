def are_anagrams(str1: str, str2: str) -> bool:
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

