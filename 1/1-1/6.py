x = input("Введите слово: ")
k = 0
for i in reversed(x):
    if (i != "ь" and i != "Ь" and i != " "):
        print(f"Последняя буква в слове: {i}")
        break
    k += 1
    if (k == len(x)):
        print("Последней буквы нет")