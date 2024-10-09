list = []
for i in range(10, 1001):
    str_i = str(i)
    if int(str_i[0]) + int(str_i[1]) == 5:
        list.append(i)
print(f"Сумма первой и второй цифры равна 5 в числах: {list}")