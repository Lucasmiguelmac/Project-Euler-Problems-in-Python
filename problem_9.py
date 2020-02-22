#c = sqrt(a**2 + b**2)
# abc = a*b*sqrt((a**2) + (b**2)
# c = 1000 — a — b
# 1000 — a — b = sqrt(a**2 + b**2)
import math
x = []
y = []
for i in range(1, 501):
    x.append(i)
    y.append(i)
for a in x:
    for b in y:
        if 1000 - a - b == math.sqrt(a**2 + b**2):
            print('Triplet: ', a, b, (1000-a-b))
            print(a*b*(1000-a-b))
