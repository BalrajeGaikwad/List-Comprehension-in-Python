'''
Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word 'odd' if the number is odd.  Result would look like ['odd','odd', 'even']
'''

"""result=[]

for n in range(20):
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)"""

result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)