from itertools import permutations
from string import printable

cnt = 0
for val in permutations(printable[:10], r=6):
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0:
        val = ''.join('*' if int(i) % 2 == 0 else '!' for i in val)
        if '**' not in val:
            cnt += 1
print(cnt)