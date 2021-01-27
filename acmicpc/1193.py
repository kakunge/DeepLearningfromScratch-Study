a = int(input())
i = 1

while True:
    if a - i <= 0:
        if i % 2 == 0:
            print(f"{a}/{i-a+1}")
            break
        else:
            print(f"{i-a+1}/{a}")
            break
    else:
        a -= i
        i += 1
