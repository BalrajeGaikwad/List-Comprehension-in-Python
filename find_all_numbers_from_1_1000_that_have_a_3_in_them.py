"""num=[]

for i in range(1,1000):
    if '3' in str(i):
        num.append(i)

print(num)"""


#By Using List cOMPREHENSION
result=[i for i in range(1,1000) if '3' in str(i)]
print(result)