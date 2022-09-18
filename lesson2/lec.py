# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+
from io import TextIOWrapper

import variable as variable

colors = ['red', 'black', 'white', 'yellow']
data = open('file.txt', 'a') # дозаписывает в конец
data.writelines(colors) # разделителей не будет
data.write('\nLINE12\n')
data.write('LINE13\n')
data.close()

# data = open('file.txt', 'w') # перезаписывает
# data.writelines(colors) # разделителей не будет
# data.close()

with open('file.txt', 'w') as data: # автоматически закрывает файл после работы, не надо data.close()
    data.write('line1\n')
    data.write('line2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()


