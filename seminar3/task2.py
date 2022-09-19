list = []
digit = False
for i in range (10):
    list.append(input("Введи что-то: "))
    if(list[i].isdigit()):
        digit = True
if(digit):
    print("Есть число!")
else:
    print("Нет числа!")

