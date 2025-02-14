'''
Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)
'''

no_dups=set()
for n in range(1,100):
    for x in range(2,10):
        if n%x ==0:
            no_dups.add(n)
print(no_dups)
print()


#nested loop

result=[num for num in range(1,100) if True in [True for x in range(2,10) if num % x==0]]
print(result)