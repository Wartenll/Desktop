def alg(N):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'
    return int(b, 2)

min_R = 10**9
for n in range(1, 1000):
    R = alg(n)
    if R > 225 and R < min_R:
        min_R = R

print(min_R)