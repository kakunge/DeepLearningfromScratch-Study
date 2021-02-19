e = 65537
p = 17
q = 23
m = 2021


N = p*q

c = pow(m, e) % N
print(c)
