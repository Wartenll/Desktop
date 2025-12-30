count = 0
for a in range(7):
    for b in range(7):
        for c in range(7):
            for d in range(7):
                for e in range(7):
                    for f in range(7):
                        for g in range(7):
                            digits = [a, b, c, d, e, f, g]
                            evens = sum(1 for d in digits if d % 2 == 0)
                            if evens == 2:
                                count += 1
print(count)