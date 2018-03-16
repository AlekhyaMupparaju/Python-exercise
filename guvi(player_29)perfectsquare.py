import math
l=int(raw_input())
r=int(raw_input())
count=0
for i in range(l,r+1):
    l=int(math.sqrt(i))
    print l,
    if i==l*l:
        count=count+1
print count
