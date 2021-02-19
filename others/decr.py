from Crypto.Util.number import inverse, getPrime, isPrime
from Crypto.Util.number import long_to_bytes, bytes_to_long

def euclidian(a, b):
    if a > b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b

    return b


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1

    return b, x0, y0


def isqrt(n):
    x = n
    y = (x+n // x) // 2
    while(y < x):
        x = y
        y = (x+n // x) // 2

    return x


def fermat(n):
    t0 = isqrt(n) + 1
    counter = 0
    t = t0 + counter
    temp = isqrt((t*t)-n)
    while((temp*temp) != ((t*t)-n)):
        counter += 1
        t = t0 + counter
        temp = isqrt((t*t)-n)
    s = temp
    p = t + s
    q = t - s

    return p, q




N = 798814300750841921713571220584672314482990450301

p = fermat(N)[0]
q = fermat(N)[1]
e = 65537


phiN = (p-1)*(q-1)

L = euclidian(p-1, q-1)


d = inverse(e, phiN)

c = 43762132500032210807139512609298331734118644679

print(pow(c, d, N))

