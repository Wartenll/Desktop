def to_base7(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s

def alg(N):
    s = to_base7(N)
    digit_sum = sum(int(d) for d in s)
    if digit_sum % 2 == 0:
        s = s + '555'
    else:
        s = '33' + s + '6'
    return int(s, 7)

max_N = 0
for n in range(1, 10000):
    R = alg(n)
    if R < 12717 and n > max_N:
        max_N = n

print(max_N)