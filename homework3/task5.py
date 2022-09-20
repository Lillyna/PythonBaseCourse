number = int(input("Input number: "))
list = [0, 1]
for i in range (2, number+1):
    list.append(list[i-2]+list[i-1])
for i in range (2, number+2):
    list.insert(0, list[1] - list[0])
print (list)
