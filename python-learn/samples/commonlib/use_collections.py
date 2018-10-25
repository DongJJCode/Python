'''
Created on Oct 25, 2018

@author: kangdongjie
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print('Point : ', p.x, p.y)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

