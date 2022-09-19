list = []
list1 = []
for i in range (4):
    list.append(input("Введи что-то: "))
str = input("Введи что надо найти: ")
if(list.__contains__(str)):
    for i in range(len(list)):
        if(list[i] == str):
            list1.append(i)
if(len(list1)>1):
    print(list1[1])
else:
    print("-1")

