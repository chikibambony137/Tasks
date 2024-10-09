dict = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
sq_sum = 0
for i in dict:
    sq_sum += pow(dict[i], 2)

print(sq_sum)