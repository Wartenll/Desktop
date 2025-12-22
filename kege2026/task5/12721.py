def convert(n):
    s = ''
    while n:
        s = str(n % 4) + s
        n //= 4
    return s or '0'


def alg(N):
    s = convert(N)
    if s[0] == '3':
        s = s.replace('1', 'x')
        s = s.replace('3', '1')
        s = s.replace('x', '3')
        s = '21' + s
    else:
        s = '1' + s[1:] + '12'
    return int(s, 4)


max_R = 0
ans = 0
for n in range(1, 1000):
    R = alg(n)
    if R < 598 and R > max_R:
        max_R = R
        ans = n

print(ans)
