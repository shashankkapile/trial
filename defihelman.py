import math
import random

print('Give prime no. : ')
q = int(input())



for x in range(1, q):
    mod = []
    found = 0
    for y in range(1, q):
        p = pow(x, y) % q
        if p in mod:
            found = 1
            break
        mod.append(p)
    if found == 0:
        a = x
        break

print('alpha : ',a)

xa = random.randint(1, q)
xb = random.randint(1, q)
print('xa : ',xa)
print('xb : ',xb)

ya = pow(a, xa) % q
yb = pow(a, xb) % q
print('ya : ', ya)
print('yb : ', yb)

k1 = pow(ya, xb) % q
k2 = pow(yb, xa) % q
print('k1 : ', k1)
print('k2 : ', k2)

if k1 == k2:
    print('found key : ',k1)
else:
    print('something went wrong !!!!')
