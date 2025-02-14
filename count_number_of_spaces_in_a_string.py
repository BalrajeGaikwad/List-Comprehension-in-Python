"""def count_s(s):
    count=0
    for char in s:
        if char ==' ':
            count+=1
    return count
input="Hello, how are you doing today?"
spaces_count=count_s(input)
print(spaces_count)"""

# by using list compherension

input="the slow solid squid swam sumptuously through the slimy swamp"
spaces=[s for s in input if s== " "]
print(len(spaces))
