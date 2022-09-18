dictionary = {}
dictionary = \
    {
        'up': 'UP',
        'down': 'DOWN'
    }
print(dictionary)
print(dictionary['up'])
for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for k in dictionary:
    print(k) # только ключи
    print(dictionary[k]) # только значения
dictionary['up'] = 'UPPP'
print(dictionary['up'])