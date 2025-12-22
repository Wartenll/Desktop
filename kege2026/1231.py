def conv(a):
    if а == 0:
        return "0"
    S=""
    while а>0:
        s = str(a%3)+s
        а = а//З
    return s
for N in range(1,100000):
    R= conv(N)
    if R%2 ==0:
        R+=R[-2:]
    else:
        R= conv(sum(map(int,R)))