from itertools import product
alph = ['А','Г','Д','И','Л','Н','Р','Я']
last_even = 0
for i, ans1 in enumerate(product(alph, repeat=6), start=1):
    if i % 2 == 0 and ans1[0] != 'Я' and ans1.count('Д') == 3:
        last_even = i
print(last_even)