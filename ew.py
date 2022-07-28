#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет
from random import randint

def game_candies():# игра для двоих людей
    print('Игра началась!')
    candies = 2021
    start_pl = randint(1,2)
    print(f'Начинает игрок под номером: {start_pl}')
    while candies > 1:
        print(f'{candies} - осталось конфет, игрок {start_pl} твой ход')
        minus = int(input('Сколько конфет вы хотите забрать(0-28)?\n'))
        while minus < 1 or minus > 28:
            minus = int(input('Некорректное число\nСколько конфет вы хотите забрать(0-28)?\n'))
        candies = candies - minus
        if candies < 0: print(f'Игра окончена, победил игрок {start_pl}')
        if start_pl == 1 : start_pl += 1
        else:start_pl-= 1





#игра с ботом
def game_candies_bot(name):
    print('Игра началась!')
    candies = 2021
    start_pl = randint(1,2)
    bot_name = 'bot'
    print(f'Начинает игрок под номером: {start_pl}')
    while candies > 1:
        if start_pl == 1:
            print(f'{candies} - осталось конфет, {name} твой ход')
            minus = int(input('Сколько конфет вы хотите забрать(0-28)?\n'))
            while minus < 1 or minus > 28:
                minus = int(input('Некорректное число\nСколько конфет вы хотите забрать(0-28)?\n'))
            candies = candies - minus
            print(f'{candies} - осталось конфет')
            if candies < 1:
                print(f'Игра окончена, победил игрок {name}'),
                return
            start_pl += 1
        if start_pl == 2:
            if candies > 0:bot_choise = randint(1,28)
            candies = candies - bot_choise
            print(f'бот взял {bot_choise} конфет(ы)')
            start_pl-= 1
            if candies < 0: print(f'Игра окончена, победил бот')


choice = int(input('1)игра с другом\n2)игра против бота\nВыберите режим игры-> '))
if choice == 1:print( game_candies())
elif choice == 2:
    name = input('Введите имя: ')
    print(game_candies_bot(name))
else:print('не тот режим')

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

a = input("Введите текст: ")
print(f"Текст после кодировки: {coding(s)}")



