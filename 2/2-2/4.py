list_str = ["aboba.html", "wfed.htm", "gjegrjf", "krk.html", "dfhtml"]
for i in list_str[::-1]:
    print(i)
    if i[-5:-1] + i[-1] != ".html":
        list_str.remove(i)

print(f"Необходимые файлы:\n{list_str}")