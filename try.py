def coll(n):
    length = 1gut
    while(n != 1):
        if (n%2 == 0):
            n//2
        else:
            n = (3*n)+1
        length += 1
    return length
def longest(limit):
    max = 0
    start = 0
    for i in range (1, 100):
        length = coll(i)
        if (length >= max):
            max = length
            start = i
    return max,start
limit = 100
l,s = longest(limit)
print(l)
print(s)