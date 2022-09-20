i = int(input("number: "))
s = []
while i>1:
    s.append(str(i%2))
    i = int(i/2)
if (i==1):
    s.append(str(i))
    s.reverse()
print(' '.join(s))


