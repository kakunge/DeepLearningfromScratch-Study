def f(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return f(x-1)+f(x-2)

n = int(input())

print(f(n))
