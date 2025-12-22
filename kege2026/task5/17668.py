def alg(N):
    b = bin(N)[2:]
    ans = b.count('1')
    if ans % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    return int(b, 2)

min_R = 10**9
for n in range(28, 1000):
    R = alg(n)
    if R < min_R:
        min_R = R

print(min_R)