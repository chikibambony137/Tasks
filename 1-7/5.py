try:
    input = str(int(input("Введите число: ")))
    result = ""
    len_input = len(input)
    for i in range(len_input):
        result += input[len_input - 1]
        len_input -= 1
    print(f"Reversed: {result}")
except:
    print("Ошибка! Введите число!")