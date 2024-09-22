#deque - double ended queue
#FIFO
#same like list but it contains endpoint

from collections import deque

#create deque
d = deque([1,2,3])
print(d)

d.append(4)
print(d)

d.appendleft(0)
print(d)

d.extend([5,6])
print(d)

print(d.pop())
print(d)