# типы данных int float boolean str list None
a = 1243
value = None
print(type(value))
print(type(a))
str = 'qwerty'
print(str) #вывод строки

s = "hello 'world'"
ss = 'hello "world"'
sss = 'hello \'wolrd\'' #эскейп-последовательности
print(sss)

print(s,'-',ss,'-',sss)
print('{} - {} - {}'.format(s,ss,sss))
print('{1} - {2} - {0}'.format(s,ss,sss))
print (f'{s} - {ss} - {sss}')#интерполяция

boo = True
print(boo)

list = []
list1 = [1,2,3,4,5,'hello']
col = [1,2,3]
print(list, list1, col)

# Арифметические операции
a = 123
b = 321
c=a+b
print(c)

a = 2
b = 8
c = a / b
c = a // b # деление целых чисел
d = a % b # остаток от деления
c = a ** b # возведение в степень

a = 1.3
b = 3
c = round(a * b, 5) # округление до 5 знаков после запятой
print(c)

a = 3
a = a + 5
a += 5 #то же самое

# Логические операции
a =1 <4 and 5<2
a=1!=2
a = 'qwe'
b = 'qwe'
print(a == b) # true
a = [1,2]
b = [1,2]
print (a == b) # true

func = 1
T = 4
x = 123
print(func<T>(x))

f = [1,2,3,4]
print(2 in f)
print(not 2 in f)

#четность числа
is_odd = not f[0] % 2
print(is_odd)

#Управляющие конструкции
#Отступы важны!!!

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

#elif = else if

#while

ori = 123
invert = 0
while ori !=0:
    invert = invert *10 + (ori % 10)
    ori //= 10
else:
    print('Пожалуй хватит')
print(invert)

#for
for i in 1,2,3,4,5:
    print(i**2)
list = [1,2,3,45,6]
for i in list:
    print(i)

for i in range(10):
    print(i)

for i in 'qwerty':
    print(i)

for i in range(1, 10, 2):
    print(i)

#Строки
#len
#in - искать подстроку
text = "dhgsahgfhhfgkhgvxcfwkygdlh"
help(text.istitle())
# срезы
print(text[0])
print(text[-5]) #пятый с конца
print(text[:]) # = print(text)
print(text[6:-18]) # c 6 до 18 с конца

#списки
ran = range(1,6)
print(type(ran))
numbers = list(ran)
print(type(numbers))

#append
#remove
#del colors[0]