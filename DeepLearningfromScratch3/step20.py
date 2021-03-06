from set import *

a = Variable(np.array(3.0))
b = Variable(np.array(2.0))
c = Variable(np.array(1.0))

y = add(mul(a, b), c)

y.backward()

print(y)#variable(7.0)
print(a.grad)#2.0
print(b.grad)#3.0

a.cleargrad()
a.cleargrad()

#__mul__ 메서드 이용
p = Variable(np.array(3.0))
q = Variable(np.array(2.0))
r = p * q

print(r)#variable(6.0)


l = Variable(np.array(3.0))
m = Variable(np.array(2.0))
n = Variable(np.array(1.0))

o = l * m + n
o.backward()

print(o)#variable(7.0)
print(l.grad)#2.0
print(m.grad)#3.0