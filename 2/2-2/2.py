list = []
num = 0
while num != "q":
    num = input("Вводите числа (\"q\" для завершения ввода): ")
    if num != "q":
        try:
            num = float(num)
            list.append(num)
        except:
            print("Введите число!")
for i in list[::-1]:
    if i <= 0:
        list.remove(i)

print(f"Список с положительными числами:\n{list}")