import math
a=int(raw_input())
b=int(raw_input())
c=a * b
if math.sqrt(c).is_integer():
    print "Yes"
else:
    print "No"
