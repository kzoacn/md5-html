import subprocess
from glob import glob
import shutil
import hashlib
import random
import string
from tqdm import tqdm


subprocess.run(["pwd"]) 

CPUS = 64
MAX_COLLISION = 200

def clear():
    for file in glob('*.txt'):
        shutil.move(file,'trash')
    for file in glob('*.gz'):
        shutil.move(file,'trash')

import datetime
import os

def _IPC(prefix,index):
    clear()
    #subprocess.run(['ls']) 
    file = 'prefix.bin'.format(index)
    with open(file,'wb') as f:
        f.write(prefix.encode())
    
    filename = 'backup/backup_collision{}.bin'.format(index)
    if os.path.exists(filename):
        print('use cache',filename)
        return open(filename,'r').read()
    
    now = datetime.datetime.now()
    print('Start TEXT COLL ...')
    print(now)
    #subprocess.run(["../scripts/textcoll.sh",file],timeout=3600) 
    subprocess.run(["timeout","1200","../scripts/textcoll.sh",file],timeout=1200) 
    shutil.copy('final_collision1.txt','backup/backup_collision{}.bin'.format(index))
    with open('final_collision1.txt','r') as f:
        return f.read()

def IPC(prefix,index):
    while True:
        try:
            ext = _IPC(prefix,index)
            new_suffix = ext[-128:]
            flag=True
            for i in range(128):
                if i==21:
                    continue

                if new_suffix[i]=='>':
                    flag=False

            if flag:
                return ext
            else:
                filename = 'backup/backup_collision{}.bin'.format(index)
                shutil.move(filename,'trash')
        except:
            print('retry')
            pass
            
def fakeIPC(prefix,index):
    random_str = [random.choice('ABCDEF'+ string.digits) for _ in range(64)]
    random_str[21]=':'
    #random_str[22]='A'
    random_str[23]='<'
    random_str[24]='C'
    random_str = ''.join(random_str)
    return prefix+random_str
    

def padding(prefix,index):
    prefix += '<PADDING_{}'.format(index)
    i = 0
    while len(prefix.encode()) % 64 !=0:
        prefix += random.choice('ABCDEFGHIIJLMNOPQRSTUVWXYZ')
        i+=1
    return prefix

html = open('index.html').read()
pos = html.find('[MD5]')
if pos==-1:
    print('Error, NO [MD5]')
prefix = html[:pos]
suffix = html[pos+5:]

prefix = padding(prefix,1926)

old_prefix = prefix

num = MAX_COLLISION

for i in tqdm(range(num)):
    prefix = IPC(prefix,i) #fakeIPC
    prefix = padding(prefix+'>',i)
prefix += '>'
