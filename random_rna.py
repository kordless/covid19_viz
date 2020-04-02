from random import random

c = "GCAT"

for x in range(29812):
    i = int(random() * 4)
    print(c[i], end = '')
