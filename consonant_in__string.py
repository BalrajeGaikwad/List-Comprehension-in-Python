'''
Create a list of all the consonants in the string "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
'''

sentence= "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

"""result=[letters for letters in sentence if letters not in 'a,e,i,o,u," ']
print(result)"""

result=[]
for char in sentence:
    vowels=['a','e','i','o','u'," "]
    if char not in vowels:
        result.append(char)

print(result)
