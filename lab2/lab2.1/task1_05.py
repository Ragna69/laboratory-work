word_1 = input('Введите первое слово:\n')
word_2 = input('Введите второе слово:\n')

word1 = list(word_1)
word2 = list(word_2)

if sorted(word1) == sorted(word2):
    print('Это аннаграммы!')
else:
    print('Это не аннаграммы.')

