
from random import randint

long_list = [randint(0, 3000) for element in range(1000000)]


n = 0
for n in 1000000:
    if (long_list[n] == -1):
        print("-1 znajduję sie na pozycji n", n)
        break
