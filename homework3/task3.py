list = [1.7, 8.01, 9.01, 8.02]
list1 = []
for i in range(len(list)):
    list1.append(list[i]%1)
list1.sort()
print(list1[-1]-list1[0])

