import math

t = int(input())
x = 0
for i in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        x = h
    else:
        x = n % h

    print(f"{x}{str(math.ceil(n/h)).zfill(2)}")
