#неизменяемый список кортеж
a, b = 3, 4 # множественное присваивание
a = (3, 4) # кортеж
print(a[0])
print(a[-1])
#a[0] = 7 # нельзя
# кортеж из одного элемента:
a = (3,)
a.

#распаковка кортежа
for item in a:
    print(item)
t = tuple(['red', 'green', 'blue'])
print(type(t))
red, green, blue = t
print(red, green, blue)
