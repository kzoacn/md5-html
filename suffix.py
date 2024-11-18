CPUS = 64
with open('backup_collision169.bin','rb') as f:
    txt = f.read()

lst = []
last = 0
seq = ''
pos = []
HEX = '0123456789ABCDEF'
p=txt.find(b'<PADDING_1926')
for i in range(p,len(txt)):
    if txt[i]==ord(':') and chr(txt[i+1]) in HEX and txt[i+2]==ord('<'):
        #print(i-last)
        seq += chr(txt[i+1])
        pos.append(i+1)
        last=i
print(len(seq))        

suffix = open('index.html','rb').read()
suffix = b'>'+suffix[suffix.find(b'[MD5]')+5:]
txt = txt + suffix

import hashlib
md5=hashlib.md5()
md5.update(txt)
print(md5.hexdigest())

md5=hashlib.md5()
new_txt=list(txt)
for p in pos:
    new_txt[p-1]=ord('>')
new_txt=bytearray(new_txt)
md5.update(new_txt)
print(md5.hexdigest())

print(txt==new_txt)

import time
from multiprocessing import Pool
from tqdm import tqdm
import random 
RANDOM = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(32)])

def f(x):
    md5=hashlib.md5()
    tmp = txt+bytes('\n<!-- MD5 Generated by https://github.com/kzoacn/md5-html - {} {} -->'.format(RANDOM,hex(x)),encoding='utf-8')
    md5.update(tmp)
    h = md5.hexdigest().upper()
    # h is a subseq of seq
    j=0
    flag=True
    for i in range(32):
        while j<len(seq) and seq[j]!=h[i]:
            j+=1
        if j>=len(seq):
            flag=False
            break
        j+=1
    return h,x,flag
    


for i in tqdm(range(3*2**10)):
    with Pool(processes=CPUS) as p:
        res = list(p.map(f, range(i*2**20,i*2**20+2**20)))
    flag=False
    for h,x,fl in res:
        if fl:
            print('Found',h,x)
            html = txt+bytes('\n<!-- MD5 Generated by https://github.com/kzoacn/md5-html - {} {} -->'.format(RANDOM,hex(x)),encoding='utf-8')
            flag=True
            break
    if flag:
        break



md5=hashlib.md5()
md5.update(html)
h=md5.hexdigest().upper()
print(h)

html=list(html)
j=0
for i in range(32):
    while j<len(seq) and seq[j]!=h[i]:
        j+=1
    html[pos[j]-1]=ord('>')
    j+=1
html=bytearray(html)
md5=hashlib.md5()
md5.update(html)
print(md5.hexdigest())

with open('new_index.html','wb') as f:
    f.write(html)
#!md5sum new_index.html