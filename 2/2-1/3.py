list = ["a", "b", "c", "d", "e", "1", "2", "3", 4, 5, 1, 3, "a", "b", "c"]
value = input("Введите значение, которое нужно удалить: ")
for i in list:
    if i == value:
        list.remove(i)
print(list)