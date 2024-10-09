str = 'abcdeabc'
new_str = ""
for i in str:
    if new_str.find(i) == -1:
        new_str += i
print(new_str)