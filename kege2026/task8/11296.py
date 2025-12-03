from itertools import product

alph = ['Д','Ж','О','С']
words = list(product(alph, repeat=6))
for i, ans1 in enumerate(words, start=1):
    if ans1[0] == 'Ж' and ans1[1] == 'С':
        print(i)
        break