a, b, c = map(int, input().split())
k = c - b

if k <= 0:
    print(-1)
else:
    print(a // k + 1)
