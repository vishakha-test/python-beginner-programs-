import array

a = array.array('i',[10,20,40,30,50])

print(a[:])
print(a[2:])
print(a[:3])
print(a[1:4])
print(a[2:10])
print(a[-10:2])
print(a[::])
print(a[::1])
print(a[::2])
print(a[2::2])
print(a[:10:3])
print(a[::-1])
print(a[-2:-5:-1])
print(a[::0])

"""output:
array('i', [10, 20, 40, 30, 50])
array('i', [40, 30, 50])
array('i', [10, 20, 40])
array('i', [20, 40, 30])
array('i', [40, 30, 50])
array('i', [10, 20])
array('i', [10, 20, 40, 30, 50])
array('i', [10, 20, 40, 30, 50])
array('i', [10, 40, 50])
array('i', [40, 50])
array('i', [10, 30])
array('i', [50, 30, 40, 20, 10])
array('i', [30, 40, 20])
Traceback (most recent call last):
  File "slicing.py", line 18, in <module>
    print(a[::0])
ValueError: slice step cannot be zero
"""


""" note: for going in forward direction stepzize should be +ve and -ve to go in backward direction if stepsize is 0 we get value error"""
