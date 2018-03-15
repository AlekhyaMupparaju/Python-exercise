n=int(raw_input())
k=int(raw_input())
a=[]
b=[]
c=[]
for i in range(n):
    d=int(raw_input())
    a.append(d)
for j in range(k):
    e=int(raw_input())
    b.append(e)
c=a+b
c.sort()
print c
print c[-k:]
