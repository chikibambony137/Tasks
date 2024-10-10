dict = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
list = []
for i in dict:
    list.append(dict[i])

print(f"Список значений словаря:\n{list}")