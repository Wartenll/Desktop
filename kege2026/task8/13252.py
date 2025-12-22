from itertools import product

digits = "0123456789ABCDEF"
count = 0

for num in product(digits, repeat=7):
    s = ''.join(num)
    if s.count('B') == 2:
        # Проверяем чередование чётных и нечётных цифр
        ok = True
        for i in range(6):
            # Чётность: 0,2,4,6,8,A,C,E - чётные; 1,3,5,7,9,B,D,F - нечётные
            # B (11) - нечётная
            d1 = int(s[i], 16) % 2
            d2 = int(s[i+1], 16) % 2
            if d1 == d2:
                ok = False
                break
        if ok:
            count += 1

print(count)