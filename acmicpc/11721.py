import math

a = input()

for i in range(math.ceil(len(a)/10)):
    print(a[i*10:i*10+10])
