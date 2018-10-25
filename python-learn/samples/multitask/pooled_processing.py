'''
Created on Oct 25, 2018

@author: kangdongjie
'''

from multiprocessing import Pool
import os
import time
import random



def long_time(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end - start)))

"""
代码貌似存在问题，并没有先建立所有进程
难道我的笔记本是单核的？
"""
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(5) :
        p.apply_async(long_time(i))
    
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    
        
        