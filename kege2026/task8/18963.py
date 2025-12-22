from itertools import product

alph = ['К', 'О', 'Т', 'Б', 'У', 'С']
ans = ['О', 'У']
cnt = 0

for val in product(alph, repeat=8):
    val = ''.join(val)
    if val[0] not in ans and 'КОТ' in val:
        cnt += 1

print(cnt)