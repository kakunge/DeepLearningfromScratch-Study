c = int(input())

for i in range(c):
    a = input().split(' ')
    a = [int (i) for i in a]
    k = a[0]
    del(a[0])
    cnt = 0

    for i in a:
        if i > sum(a[0:len(a)])/k:
            cnt += 1
    print('%.3f%s' % ((cnt/len(a)*100), '%'))
