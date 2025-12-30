from itertools import product

alph = ['Е','Л','О','П','Р','С','Т']
ans= ['Е','О']

count = 0
for i, val in enumerate(product(alph, repeat=5), start=1):
    if val[-1] in ans:
        val_count = sum(1 for ans1 in val if ans1 not in ans)
        if val_count <= 3 and i % 2 == 1:
            count += 1

print(count)