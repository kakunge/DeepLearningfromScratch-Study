t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    p, q = 1, 1
    cnt = 0
    k = y - x
    
    
    while True:
        if k <= 0:
            print(cnt)
            break
        elif q % 2 == 0:
            k -= p
            cnt += 1
            p += 1
            q += 1
        elif q % 2 != 0:
            k -= p
            cnt += 1
            q += 1
