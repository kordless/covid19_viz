from random import random

c = "GCAT"

for x in range(49182):
    i = int(random() * 4)
    print(c[i], end = '')
