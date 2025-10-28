word = input("Введите слово палиндром:")
if not word:
    print('Строка пустая!')
else:
    wordlower = word.lower()
    if wordlower == wordlower[::-1]:
        print('Это слово - палиндром!')
    else:
        print('Это слово не палиндром.')
