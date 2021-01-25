a = int(input())
h = 6
i = 1

while True:
    if a == 1:
        print(i)
        break
    elif a - h > 0:
        a = a - h
        h += 6
        i += 1
    else:
        print(i+1)
        break
