from itertools import product
alph= sorted('БМЮРН')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    if pos % 2 == 1 and 'М' not in :
        cnt += 1
print(cnt)