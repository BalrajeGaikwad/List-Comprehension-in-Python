'''Find all of the words in a string that are less than 4 letters'''

sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'

examine=sentence.split()

result=[word for word in examine if len(word) >=4]
print(result)