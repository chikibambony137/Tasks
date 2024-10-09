try:
    input = str(int(input("Введите число: ")))
    sum = 0
    for i in input:
        sum += int(i)
    print(f"Сумма цифр числа равна {sum}")
except:
    print("Ошибка! Введите число!")