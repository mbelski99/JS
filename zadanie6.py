di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}

import copy
di_c=copy.deepcopy(di)
di['four'][0]='cztery'
print(di)
print(di_c)