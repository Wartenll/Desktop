def alg(N):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    return int(b, 2)


max_N = 0
for n in range(1, 100):
    R = alg(n)
    if R < 30 and n > max_N:
        max_N = n

print(max_N)
