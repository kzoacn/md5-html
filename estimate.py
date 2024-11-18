from decimal  import Decimal

mem=[[-1 for i in range(500)] for j in  range(500)]

def dfs(n,m):
    if m==0:
        return Decimal(1)
    if n<m:
        return Decimal(0)
    if mem[n][m]!=-1:
        return mem[n][m]
    res = Decimal(1/16)*dfs(n-1,m-1) + Decimal(15/16)*dfs(n-1,m)
    mem[n][m]=res
    return res

from math import *
print(log(dfs(128,32),2))
print(log(dfs(150,32),2))
print(log(dfs(200,32),2))
print(log(dfs(256,32),2))

text=''.join(['a' for i in range(1024*25)])

import hashlib


import time
from multiprocessing import Pool


start = time.time()

def f(x):
    md5=hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()


with Pool(processes=64) as p:
    res = list(p.map(f, range(2**20)))

end = time.time()
print(end - start)
