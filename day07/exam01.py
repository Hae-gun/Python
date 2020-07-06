keys = map(str,input().split())
values = map(float, input().split())

#keys = list(keys)
#values = list(values)
#print(keys)
#print(values)

unit = dict(zip(keys,values))

print(unit)
