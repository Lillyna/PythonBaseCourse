list1 = [1,2,3,4]
list2 = list1
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

list1[0] = 123 # значения меняются в обоих списках
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

print(list1.pop())
print(list1)
print(len(list1))
print(list1.pop(2))
print(list1, list2)
print(list1.insert(1, 11))
list1.append(33)
print(list2)
