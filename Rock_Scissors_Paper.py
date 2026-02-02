def StSkPa_game():
    import random
    import time

    def get_answer():
        while True:
            try:
                player = int(input("Выбери: 1) Камень. 2) Ножницы. 3) Бумага. Ответ: "))
                if player not in (1, 2, 3):
                    print("Введи ответ корректно!")
                    continue
                return player
            except ValueError:
                print("Что ты делаешь?")

    player_win_count = 0
    computer_win_count = 0
    choices = {1: "Камень", 2: "Ножницы", 3: "Бумага"}

    print("Привет!")
    time.sleep(1)
    print("Поиграем в Камень-Ножницы-Бумага?")
    time.sleep(1)
    print("Правила просты: ")
    time.sleep(1)
    print("Играем до трёх побед.")
    time.sleep(1)
    print("Начинаем...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    print("...")
    time.sleep(1)

    while True:
        player_round_win_count = 0
        computer_round_win_count = 0

        while player_round_win_count < 3 and computer_round_win_count < 3:
            computer = random.randint(1, 3)
            print("Счёт:", player_round_win_count, computer_round_win_count)
            time.sleep(1)
            player = get_answer()
            time.sleep(1)
            if player == 1:
                print("Игрок: Камень.")
            elif player == 2:
                print("Игрок: Ножницы.")
            else:
                print("Игрок: Бумага.")

            time.sleep(1)

            if computer == 1:
                print("Компьютер: Камень.")
            elif computer == 2:
                print("Компьютер: Ножницы.")
            else:
                print("Компьютер: Бумага.")

            if player == computer:
                time.sleep(1)
                print("Ничья!")
            elif (player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1):
                time.sleep(1)
                print("Ты победил этот раунд!")
                player_round_win_count += 1
            else:
                time.sleep(1)
                print("Ты проиграл этот раунд!")
                computer_round_win_count += 1

            if player_round_win_count == 3:
                time.sleep(1)
                print("Ты победил!")
                player_win_count += 1
                again = input("Хочешь сыграть снова? Да/Нет: ").lower()
                if again != "да":
                    print("Удачи! Итоговый счёт:", player_win_count, ":", computer_win_count)
                    exit()
            if computer_round_win_count == 3:
                time.sleep(1)
                print("Ты проиграл!")
                computer_win_count += 1
                again = input("Хочешь сыграть снова? Да/Нет: ").lower()
                if again != "да":
                    print("Удачи! Итоговый счёт:", player_win_count, ":", computer_win_count)
                    exit()


game3 = StSkPa_game()