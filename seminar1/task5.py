a = str(input('введи число дробное с запятой: '))
if (a.__contains__(',')):
    print (a[a.index(',')+1])
else:
    print ('нету')