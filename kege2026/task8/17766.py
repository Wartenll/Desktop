from itertools import product

alph = sorted('СЕНТЯБРЬ')
res = 0

for pos, val in enumerate(product(alph, repeat=5), start=1):
    if pos % 2 == 0 and val[0] == 'Р' and 'Ь' not in val:
        res = pos
        val = ''.join(val)

print(res)
