import random

def get_num():
    return random.randint(1, 11)

def play_game():
    print('--------------------')
    print('         21*        ')
    print('--------------------')
    print('hit  | бросить кости')
    print('hold | хватит')
    print('--------------------')

    player = 0
    diller = 0

    while True:
        choise = input('hit or hold? ')
        print('**********************')

        if choise == 'hit':
            a = get_num()
            player += a
            print(f'Вам выпало {a}')
            print(f'Ваши очки: {player}')
            print('**********************')
            if player > 21:
                print('---------------------')
                print(f'Победитель DIller!!!')
                print(f'Вы проиграли. У вас {player} :(')
                print('---------------------')
                return
        elif choise == 'hold':
            print(f'((Ваши очки {player}))')
            break

    while diller < 17:
        a = get_num()
        diller += a
        print(f'Очки Diller {diller}')
    print('---------------')
    if diller > 21:
        print('---------------')
        print(f'Diller перебрал у него {diller} очков')
        print('Поздравляю, вы выйграли!')
        print('---------------')
    elif diller > player:
        print('---------------')
        print('Diller выйграл')
    elif player > diller:
        print('---------------')
        print('Поздравляю вы выйграли!!!!!!')
        print('---------------')
    elif diller == player:
        print('---------------')
        print('*** НИЧЬЯ ***')
        print('---------------')








while True:  #Функция бесконечного запуска игры
    play_game()
    print('-----------------------------------')
    input('Нажмите enter, чтобы начать заного')