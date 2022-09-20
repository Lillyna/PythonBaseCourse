list = [1,2,3,4,5,6,7,8,9]
list1 = []
for i in range(1,int((len(list)+3)/2)):
    list1.append(list[i-1]*list[-i])
print(list1)