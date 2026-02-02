import random
import time

print("Компьютер загадывает число от 1 до 10.")
time.sleep(1)
print("...")
time.sleep(1.5)
print("У Игрока 3 попытки угадать.")
time.sleep(1)
print("Победа - выход. Неудача - подсказка:")
time.sleep(0.5)
print("*больше")
time.sleep(0.5)
print("*меньше")
time.sleep(2)
print("...")
time.sleep(1)
ready = input("Ты готов? Да/Нет: ").lower()
if ready != "да":
    print("Конец.")
    exit()
else:
    print("Начинаем...")
    time.sleep(1)

win_count = 0
while True:
    secret = random.randint(1,10)
    attempts = 3
    while attempts > 0:
        time.sleep(1)
        print("Попыток: ", attempts)

        while True:
            try:
                guess = int(input("Число: "))
                if guess > 10 or guess < 1:
                    time.sleep(1)
                    print("Число должно быть от 1 до 10!")
                    continue
                break
            except ValueError:
                time.sleep(1)
                print("Эй! Используй цифры!")
        attempts -= 1
        if guess == secret:
            print("...")
            time.sleep(1)
            print("Ты победил!")
            win_count += 1
            print("Счетчик побед:", win_count)
            break
        elif guess < secret:
            if attempts > 0:
                print("...")
                time.sleep(1)
                print("*больше")
        else:
            if attempts > 0:
                print("...")
                time.sleep(1)
                print("*меньше")

        if attempts == 0:
            time.sleep(1)
            print("Ты проиграл. Верное число было... ", secret)

    time.sleep(1)
    again = input("Хочешь попробовать снова? ").lower()
    if again != "да":
        time.sleep(1)
        print("Удачи! Твой итоговый счёт побед:", win_count)
        exit()
        