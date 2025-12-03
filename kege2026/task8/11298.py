from itertools import product
alph=['А','Ж','З','О','П','Ю']
cnt = 0
for i, ans1 in enumerate(product(alph, repeat=6), start=1):
    if i % 2 == 0 and ans1[0] == 'А' and ans1.count('З') >= 2:
        cnt += 1
print(cnt)