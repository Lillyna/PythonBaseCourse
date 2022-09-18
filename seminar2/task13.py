str1 = input('Введите строку: ')
str2 = input('Введите строку: ')
if(str1 in str2):
    print(str2.count(str1))
elif(str2 in str1):
    print(str1.count(str2))
else:
    print('нет вхождений')