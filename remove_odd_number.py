"""numbers=[10,3,4,5,6,7,5,4,0,5,6,4,5,6,4,4,5]
result=[]
for i in lst:
    if i %2==0:
        result.append(i)

print(result)"""

numbers=[10,3,4,5,6,7,5,4,0,5,6,4,5,6,4,4,5]
result=[num for num in numbers if num %2==0]
print(result)