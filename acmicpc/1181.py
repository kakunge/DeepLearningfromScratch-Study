n = int(input())
a = []
for i in range(n):
    a.append(input())
a = sorted(list(set(a)), key=lambda x: (len(x), x))

for i in range(len(a)):
    print(a[i])
