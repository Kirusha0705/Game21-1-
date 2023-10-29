import random

diller = 0
player = 0


def get_num():
    return random.randint(1, 11)  #Получить псевдо-рандомное число


def game_player():
    global player
    a = get_num()
    player += a
    print('------------------')
    print(f'|Тебе выпало: {a}')
    print(f'|У тебя: {player}')
    print('------------------')
    if player >= 21:
        return win_lose_player()


def game_diller():
    global diller
    a = get_num()
    diller += a
    print(f'Diller: {diller}')
    if diller >= 21:
        return win_lose_diller()


def win_lose_player():
    if player == 21:
        print(f'Количество очков {player} Вы выиграли!')
    elif player > 21:
        print(f'Количество очков {player}. ВЫ набрали больше 21. Вы проиграли!!!')


def win_lose_diller():
    if diller == 21:
        print(f'ВЫ проиграли, Diller набрал {diller} очков')
    elif diller > 21:
        print(f'Поздравляем!!! Diller перебрал у него {diller} очков')


def noone():
    if player > diller and player <= 21 and diller != 0:
        print(f'Вы победили. У вас Player = {player} > Diller = {diller}')
    elif diller > player and diller <= 21:
        print(f'Вы проиграли. Diller = {diller} > Player = {player}')
    elif diller > 0 and player > 0:
        print(f'НИЧЬЯ!!! Diller = {diller} == Player = {player}')


while player < 21:
    ask = input('hit or stop? ')
    if ask == 'hit':
        game_player()
    else:
        break

while diller < 21:
    if diller < 16 and player < 21:
        game_diller()
    else:
        noone()
        break


