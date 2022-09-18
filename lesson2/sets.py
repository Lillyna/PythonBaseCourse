colors = {'red', 'blue'}
print(type(colors))
print(colors)
colors.add('red')
colors.add('grey')
print(colors)
colors.remove('red')
#colors.remove('red') #KeyError: 'red'
colors.discard('red')
print(colors)
colors.clear()
print(colors)

a = {1,2,3,4,5}
b = {3,4,5,6,6}
q = a\
    .union(b)\
    .difference(a.intersection(b))
print(q)

s = frozenset(a)