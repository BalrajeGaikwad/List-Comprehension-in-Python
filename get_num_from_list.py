'''
Get only the numbers in a sentence like 'In 1984 there were 13 instances of a protest with over 1000 people attending'.  Result is a list of numbers like [3,4,5]
'''

sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

words=sentence.split()
result=[num for num in words if not num.isalpha()]
print(result)



re=[]
for num in words:
    if not num.isalpha():
        re.append(num)

print(re)
