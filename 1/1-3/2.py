ab = input("Введите два целых числа: ")

try:
    ab = ab.split(", ")
    if int(ab[0]) % int(ab[1]) == 0:
        print("True")
    else:
        print("False")
except:
    print("Ошибка! Введите целые числа!")