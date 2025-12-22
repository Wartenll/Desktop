def alg(N):
    b = bin(N)[2:]
    ones = b.count('1')
    if ones % 2 == 0:
        b = '11' + b[2:] + '1'
    else:
        zeros = b.count('0')
        b += '0' if zeros < ones else '1'
    return int(b, 2)
n = 1
while True:
    if alg(n) > 271:
        print(n)
        break
    n += 1