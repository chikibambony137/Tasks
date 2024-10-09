while True:
    x = input("Введите два слова через пробел: ").split(" ")
    if (len(x) != 2):
        print("Ошибка! Введите правильное количество слов!")
    else:
        break
first_word = x[0]
second_word = x[1]
if (first_word[0] == second_word[0]):
    print(f"Первые буквы слов совпадают (\"{first_word[0]}\")")
else:
    print(f"Первые буквы слов не совпадают (\"{first_word[0]}\" и \"{second_word[0]}\")")