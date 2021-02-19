from Crypto.Util.number import inverse, getPrime, isPrime

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


p = 261991186766878479653593750921882040969
q = 257912153455962639186293517651778582187
e = 65537


N = p*q
phiN = (p-1)*(q-1)

L = euclidian(p-1, q-1)


d = inverse(e, phiN)
