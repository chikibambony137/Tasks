ab = input("Введите два целых числа: ")
try:
    ab = ab.split(", ")
    a = int(ab[0])
    b = int(ab[1])
    print(f"Остаток от деления {a} на {b} равен {a % b}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except:
    print("Ошибка!")