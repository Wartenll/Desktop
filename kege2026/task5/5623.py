def alg(N):
    b = bin(N)[2:]
    ans = b.count('1')
    if ans % 2 == 0:
        b = '1' + b[:-2] + '10'
    else:
        b = '10' + b[2:] + '1'
    return int(b, 2)


n = 1
while True:
    if alg(n) > 202:
        print(n)
        break
    n += 1
