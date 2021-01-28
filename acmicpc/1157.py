import string as s
a, b = [], []
c = list(input().upper())

for i in c:
    if i in a:
        pass
    else:
        a.append(i)
        b.append(c.count(i))

if b.count(max(b)) == 1:
    print(a[b.index(max(b))])
else:
    print('?')
