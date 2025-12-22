from itertools import product
alph= ['А,В,Т,О,Р']
for pos, val in enumerate(product(alph, repeat =4), start=1):

    val = ''.join(val)
    if val == 'ВАТА':
        print(pos)
        break