list = [1.456, 2.125, 3.32, 4.1, 5.34]
list[:] = [round(i, 1) for i in list]

print(list)