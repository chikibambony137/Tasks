list = []
element = ""
while element != "q":
    element = input("Введите значения элементов списка (\"q\", чтобы закончить): ")
    list.append(element)
new_list = []
for i in list:
    if i[:7] == "http://":
        new_list.append(i)
    
print(f"Ссылки: {new_list}")