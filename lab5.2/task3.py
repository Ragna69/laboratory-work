def is_palindrome(value) -> bool:
    s = str(value).strip().lower()
    return s == s[::-1]

