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
count = 0
for i in list:
    if i < 0:
        count += 1
print(f"Отрицательных чисел в списке: {count}\n{list}")