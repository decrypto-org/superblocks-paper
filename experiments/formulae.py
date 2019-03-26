import math
import bigfloat
from bigfloat import BigFloat, precision

MAX_MU = 100

def choose(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def bigchoose(n,r):
    f = bigfloat.factorial
    return f(n) / f(r) / f(n-r)

def f1(n, mu):
    s1 = 0
    for i in range(1, n + 1):
        p = 2**(-mu)
        for j in range(i + 1, n + 1):
            s2 = 0
            for mup in range(1, mu):
                s2 += 2**(-mup)
            p *= s2
        s1 += p
        # print(s1)
    return s1

def f2(n, mu):
    s1 = 0
    for i in range(1, n + 1):
        p = 2**(-mu)
        for j in range(i + 1, n + 1):
            p *= (1 - 2**(1 - mu))
        s1 += p
        # print(s1)
    return s1

def f3(n, mu):
    s1 = 0
    for i in range(1, n + 1):
        s1 += (1 - 2**(1 - mu))**(n - i)
    return 2**(-mu) * s1

def f35(n, mu):
    s1 = 0
    for i in range(1, n + 1):
        s1 += (1 - 2**(1 - mu))**(-i)
    return 2**(-mu) * (1 - 2**(1 - mu))**n * s1

def f36(n, mu):
    s1 = 0
    for i in range(0, n):
        s1 += (1 - 2**(1 - mu))**(-(i + 1))
    return 2**(-mu) * (1 - 2**(1 - mu))**n * s1

def f37(n, mu):
    s1 = 0
    for i in range(0, n):
        s1 += (1 - 2**(1 - mu))**(-i)
    return 2**(-mu) * (1 - 2**(1 - mu))**n / (1 - 2**(1 - mu)) * s1

def f4(n, mu):
    n1 = (1 - 2**(1 - mu))**n
    n2 = 1 - (1 - 2**(1-mu))**(-n)
    d1 = 1 - 2**(1 - mu)
    d2 = 1 - (1 - 2**(1 - mu))**(-1)
    numerator = n1 * n2
    denominator = d1 * d2
    return 2**(-mu) * numerator / denominator

def f5(n, mu):
    return (1.0/2)*(1 - (1 - 2**(1 - mu))**n)

def f6(n):
    s1 = 0
    s3 = 0
    # s35 = 0
    # s36 = 0
    # s37 = 0
    # s4 = 0
    s5 = 0
    # terms = ''
    for mu in range(1, MAX_MU):
        Bnmu1 = f1(n, mu)
        Bnmu3 = f3(n, mu)
        # Bnmu35 = f35(n - 1, mu)
        # Bnmu36 = f36(n - 1, mu)
        # Bnmu37 = f37(n - 1, mu)
        # Bnmu4 = f4(n - 1, mu)
        Bnmu5 = f5(n, mu)
        # terms += ', ' + str(Bnmu5)
        s1 += Bnmu1
        s3 += Bnmu3
        # s35 += Bnmu35
        # s36 += Bnmu36
        # s37 += Bnmu37
        # s4 += Bnmu4
        s5 += Bnmu5
    # print('n = ', n, 's1 = ', s1)
    # print('n = ', n, 's3 = ', s3)
    # print('terms = ', terms)
    # print('n = ', n, 's35 = ', s35)
    # print('n = ', n, 's36 = ', s36)
    # print('n = ', n, 's37 = ', s37)
    # print('n = ', n, 's4 = ', s4)
    # print('n = ', n, 's5 = ', s5)
    return s5

def f63(n):
    s1 = 0
    for mu in range(1, MAX_MU):
        s1 += 1 - (1 - 2**(1 - mu))**n
    return 1.0/2 * s1

def f64(n):
    s1 = 0
    for mu in range(1, MAX_MU):
        s2 = 0
        for i in range(0, n + 1):
            s2 += choose(n, i) * 1**(n - i) * (-2**(1 - mu))**i
        s1 += 1 - s2
    return 1.0/2 * s1

def f65(n):
    s1 = 0
    for mu in range(1, MAX_MU):
        s2 = 0
        for i in range(1, n + 1):
            s2 += choose(n, i) * 1**(n - i) * (-2)**((1 - mu) * i)
        s1 += -s2
    return 1.0/2 * s1

def f66(n):
    s1 = BigFloat(0)
    for mu in range(1, MAX_MU):
        s2 = BigFloat(0)
        for i in range(0, n + 1):
            s2 += bigchoose(n, i) * (-(2**(1 - mu))) ** i
        s1 += 1 - s2
    return 1.0/2 * s1

def f67(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s1 = BigFloat(0)
    for mu in range(1, MAX_MU):
        s2 = BigFloat(0)
        for k in range(0, even_bound + 1):
            s2 += bigchoose(n, 2*k) * 2**((1 - mu) * 2*k)
        s3 = BigFloat(0)
        for k in range(0, odd_bound + 1):
            s3 += bigchoose(n, 2*k + 1) * 2**((1 - mu) * (2*k + 1))
        s1 += 1 - s2 + s3
    return 1.0/2 * s1

def f68(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s1 = BigFloat(0)
    for mu in range(1, MAX_MU):
        s2 = BigFloat(0)
        for k in range(1, even_bound + 1):
            s2 += bigchoose(n, 2*k) * 2**((1 - mu) * 2*k)
        s3 = BigFloat(0)
        for k in range(0, odd_bound + 1):
            s3 += bigchoose(n, 2*k + 1) * 2**((1 - mu) * (2*k + 1))
        s1 += -s2 + s3
    return 1.0/2 * s1

def f69(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s1 = BigFloat(0)
    for mu in range(1, MAX_MU):
        s2 = BigFloat(0)
        for k in range(0, odd_bound + 1):
            s2 += bigchoose(n, 2*k + 1) * 2**((1 - mu) * (2*k + 1))
        s3 = BigFloat(0)
        for k in range(1, even_bound + 1):
            s3 += bigchoose(n, 2*k) * 2**((1 - mu) * 2*k)
        s1 += s2 - s3
    return 1.0/2 * s1

def f7(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s1 = BigFloat(0)
    for k in range(0, odd_bound + 1):
        for mu in range(1, MAX_MU):
            s1 += bigchoose(n, 2*k + 1) * 2**((1 - mu)*(2*k+1))

    s2 = BigFloat(0)
    for k in range(1, even_bound + 1):
        for mu in range(1, MAX_MU):
            s2 += bigchoose(n, 2*k) * 2**((1 - mu)*2*k)

    return 1.0/2 * (s1 - s2)

def f71(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s10 = BigFloat(0)
    for k in range(0, odd_bound + 1):
        s1 = BigFloat(0)
        for mu in range(1, MAX_MU):
            s1 += 2**((1 - mu)*(2*k+1))
        s10 += bigchoose(n, 2*k + 1) * s1

    s20 = BigFloat(0)
    for k in range(1, even_bound + 1):
        s2 = BigFloat(0)
        for mu in range(1, MAX_MU):
            s2 += 2**((1 - mu)*2*k)
        s20 += bigchoose(n, 2*k) * s2

    return 1.0/2 * (s10 - s20)

def f72(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s10 = BigFloat(0)
    for k in range(0, odd_bound + 1):
        s1 = BigFloat(0)
        for mu in range(1, MAX_MU):
            s1 += (2**(2*k+1))**(-mu)
        s10 += bigchoose(n, 2*k + 1) * 2**(2*k + 1) * s1

    s20 = BigFloat(0)
    for k in range(1, even_bound + 1):
        s2 = BigFloat(0)
        for mu in range(1, MAX_MU):
            s2 += (2**(2*k))**(-mu)
        s20 += bigchoose(n, 2*k) * 2**(2*k) * s2

    return 1.0/2 * (s10 - s20)

def f73(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s10 = BigFloat(0)
    for k in range(0, odd_bound + 1):
        s1 = BigFloat(0)
        for mu in range(0, MAX_MU):
            s1 += (2**(2*k+1))**(-mu)
        s10 += bigchoose(n, 2*k + 1) * 2**(2*k + 1) * (s1 - 1)

    s20 = BigFloat(0)
    for k in range(1, even_bound + 1):
        s2 = BigFloat(0)
        for mu in range(0, MAX_MU):
            s2 += (2**(2*k))**(-mu)
        s20 += bigchoose(n, 2*k) * 2**(2*k) * (s2 - 1)

    return 1.0/2 * (s10 - s20)

def f74(n):
    odd_bound = int(math.floor((n - 1) / 2))
    even_bound = int(math.floor(n / 2))

    s10 = BigFloat(0)
    for k in range(0, odd_bound + 1):
        s1 = 1 / (1 - 2**(-(2*BigFloat(k) + 1)))
        s10 += bigchoose(n, 2*k + 1) * 2**(2*k + 1) * (s1 - 1)

    s20 = BigFloat(0)
    for k in range(1, even_bound + 1):
        s2 = 1 / (1 - 2**(-2*BigFloat(k)))
        s20 += bigchoose(n, 2*k) * 2**(2*k) * (s2 - 1)

    return 1.0/2 * (s10 - s20)

def f75(n):
    s = BigFloat(0)
    for i in range(1, n + 1):
        expr = 1 / (1 - 2**BigFloat(-i)) - 1
        s += bigchoose(n, i) * 2**i * (-1)**(i+1) * expr

    return 1.0/2 * s

def f76(n):
    s = BigFloat(0)
    for i in range(1, n + 1):
        expr = 2**i / (2**i - 1)
        s += bigchoose(n, i) * (-1)**(i+1) * expr

    return 1.0/2 * s

with precision(200):
  for n in range(1, 100):
     print('n = ', n, 'f6 = ', f6(n), ', f74 = ', f74(n), ', f76 = ', f76(n), ', f = ', 0.480898346 * math.log(n) + 1)
# f66(n)
# f67(n)
