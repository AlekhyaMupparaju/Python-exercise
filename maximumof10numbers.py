m=[]
n=int(raw_input())
for i in range(0,n):
    b=int(raw_input())
    m.append(b)
m.sort()
print m[n-1]
