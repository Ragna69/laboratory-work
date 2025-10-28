import random

random = random.randint(1,100)
answer = 0
print('Программа загадала число от 1 до 100, попробуй угадать его.')
while answer != random:
    answer = int(input('Твой вариант:'))
    if answer > random:
        print('Меньше')
    elif answer < random:
        print('Больше')
    else:
        print('Ты угадал!')
