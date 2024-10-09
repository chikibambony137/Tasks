x = 0
ab = input("Введите диапазон чисел (через запятую и пробел): ")
try:
    ab = ab.split(", ")
    a = int(ab[0])
    b = int(ab[1])
    for i in range(a, b + 1):
        if (i % 2 == 1):
            x += i
    print(f"Сумма чисел от {a} до {b} равно: {x}")
except:
    print("Ошибка")