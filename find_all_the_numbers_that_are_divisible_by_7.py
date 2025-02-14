
lst=[]
for i in range(1,1000):
    if i %7==0:
        lst.append(i)

print(lst)

#by using list compherension

div7=[n for n in range(1,1000) if n%7==0]
print(div7)