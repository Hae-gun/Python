x = input().split()
x = list(x)
# del x[len(x):len(x)-6:-1]
del x[-5:]
x = tuple(x)
print(x)
