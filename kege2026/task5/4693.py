def alg(N):
    b = bin(N)[2:]
    ans = b.count('1')
    if ans % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    return int(b, 2)


n = 1
while True:
    if alg(n) > 40:
        print(n)
        break
    n += 1
