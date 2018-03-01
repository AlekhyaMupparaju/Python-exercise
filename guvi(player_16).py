import collections
s=int(raw_input())
a=[]
for i in range(s):
    b=int(raw_input())
    a.append(b)
results = collections.Counter(a)
print min(results,key=results.get)
