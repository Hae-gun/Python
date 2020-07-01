# a = [0,10,20,30,40,50,60,70,80,90]
# print(30 in a)
# print(100 in a)
# print(30 not in a)
## print(100 not in a)

##43 in (38,76,43,62,19)
##1 in range(10)
##'P' in 'Hello, Python'
##a = [0,10,20,30]
##b=  [9,8,7,6]
##a+b
##[0, 10, 20, 30, 9, 8, 7, 6]

## range는 +연산 불가능
## range(0, 10) + range(10, 20)
## list(range(0,10)) + list(range(10,20))
## tuple(range(0,10)) + tuple(range(10,20))
##'Hello, ' + 'world!'

##'hello'+3
##Traceback (most recent call last):
##  File "<pyshell#18>", line 1, in <module>
##    'hello'+3
##TypeError: can only concatenate str (not "int") to str
##'hello'+str(3)

##[0,1,2,3,4,5] * 3
##3 * [ 0,1,2,3,4,5]

##'hello, '*3
##a = [0,10,20,30,40,50,60,70,80,90]
##len(a)

##len(range(0,10,2))
##len('hello world!')

##hello = '안녕하세요'
##len(hello.encode('utf-8'))

##a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
##a[0]
##a[1]
##a[2]

##b = (38,21,53,62,19)
##b[0]
##r = range(0,10,2)
##r[2]
##hello = 'Hello, world!'
##hello[7]
##a = [38,21,53,62,19]
##a.__getitem__(1)

##a[-1]
##a[-5]

##a = [1,3,5,7,9]
##a[len(a)-1]

##a = [0,0,0,0,0]
##a[0] = 38
##a[1] = 21
##a[2] = 53
##a[3] = 62
##a[4] = 19

##a = [0,10,20,30,40,50,60,70,80,90]
##a[0:4]
##a[1:1]
##a[4:7]
##a[4:-1]
##a[2:8:3]

##a[:7]
##a[7:]
##a[:]

##a[:7:2]
##a[4::2]
##a[::2]
##a[::]

##a[0:len(a)]
##a[:len(a)]

b = (0,10,20,30,40,50,60,70,80,90)
b[4:7]
b[4:]
b[:7:2]
r = range(10)
r[4:7]
r[4:]
r[:7:2]
list(r[:7:2])

hello = 'Hello, world!'
hello[2:9]
hello[:9:2]

range(10)[slice(4,7,2)]
range(10).__getitem__(slice(4,7,2))

a = [0,10,20,30,40,50,60,70,80,90]
s = slice(4,7)
a[s]

r = range(10)
r[s]
hello = 'Hello, world!'
hello[s]

a[2:5] = ['a','b','c']

a[2:5] = ['a']
a[2:5] = ['a','b','c','d']
a[2:8:2] = ['a','b','c']
a[2:8:2] = ['a','b']

del a[2:5]
del a[2:8:2]
