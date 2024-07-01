number = (input("Number: "))

num = 0
for n in number:
    num = num + 1
    if n == ".":
        num = num - 1
    else: 
        num = num + 0
print(num) 




