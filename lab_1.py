def factorization(n):
    p = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            p[d] = p.get(d,0) + 1
            n //= d
        d += 1
    if n > 1:
        p[n] = p.get(n,0) + 1
    return p
 
 
a = int(input("input A: "))
b = int(input("input B: "))
pa = factorization(a)
pb = factorization(b)
n = 1
for key in pa :
    if not key in pb :
        n = -1
        break
    k = -(-pa[key]//pb[key])
    if k > n :
        n = k 
print(n)
