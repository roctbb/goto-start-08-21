from random import randint

print("Вы приехали в Лагерь GoTo")
input()
print("Вы хотите есть.")
input()
print("Пойти в столовую (1) или заселиться (2)?")
answer = input()

if answer == "1":
    print("Вы в столовой. Будете мыть руки? (1) - да / (2) - нет")
    is_clean = input()
    if is_clean == "2":
        a = randint(1, 2)
        if a == 1:
            print("Вы попытались прошмыгнуть мимо врача, но вас поймали"
                  "и заставили помыть руки.")
        else:
            print("Вы проскользнули мимо врача.")

if answer == "2":
    print("Вы пошли заселяться")