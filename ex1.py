import random


def roll_dice():
    return random.randint(1, 11)


def play_game():
    print("---------------------")
    print("         21*         ")
    print("---------------------")
    print(" Дилер должен бросать")
    print(" пока у него < 17. ")
    print("---------------------")

    player_score = 0
    dealer_score = 0

    while True:
        print("hit  | Бросить кости")
        print("hold | Остановиться ")
        print("---------------------")
        choice = input(f"{player_score} > ")

        if choice == "hit":
            dice_roll = roll_dice()
            player_score += dice_roll
            print(f"Игрок* {player_score}")
            if player_score > 21:
                print("---------------------")
                print("Игрок перебрал! Дилер выиграл!")
                return

        elif choice == "hold":
            print("---------------------")
            print(f"Игрок: {player_score}")
            break

    while dealer_score < 17:
        dice_roll = roll_dice()
        dealer_score += dice_roll
        print(f"Дилер* {dealer_score}")

    print("---------------------")
    print(f"Дилер: {dealer_score}")
    if dealer_score > 21:
        print("---------------------")
        print("Дилер перебрал! Игрок выиграл!")
    elif dealer_score > player_score:
        print("---------------------")
        print("Дилер победил!")
    elif dealer_score == player_score:
        print("---------------------")
        print("Ничья!")
    else:
        print("---------------------")
        print("Игрок победил!")


while True:
    play_game()
    input("Нажмите enter чтобы играть заново...")
