"""def eg(sentence):
    vowels='aeiou'
    filtered=[]
    for l in sentence:
        if l not in vowels:
            filtered.append(l)
    return "".join(filtered)

sentence = 'My name is Aarshay Jain!'
print ("FOR-loop result: " + eg(sentence))
print ("LC result      : " + eg(sentence))"""


def eg(sentence):
    vowels='aeiou'
    return''.join(l for l in sentence if l not in vowels)
sentence = 'My name is Aarshay Jain!'
print ("LC result      : " + eg(sentence))