
'''
Find the common numbers in two lists (without using a tuple or set) list_a = [1, 2, 3, 4], list_b = [2, 3, 4, 5]
'''

lista=[2,3,4,5,6]
listb=[3,4,56,6,7]

common=[a for a in lista if a in listb]
print(common)


result=[]
for a in lista:
    if a in listb:
        result.append(a)

print(result)
