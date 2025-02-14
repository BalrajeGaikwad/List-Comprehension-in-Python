'''
 Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].  Result would look like [(index, value), (index, value)]
 '''

"""items=["hi", 4, 8.99, "apple", ('t,b','n')]
result=[(index, item) for index , item in enumerate(items)]
print(result)"""


items=["hi", 4, 8.99, "apple", ('t,b','n')]
result=[]

for index, item in enumerate(items):
    result.append((index,item))
print(result)

