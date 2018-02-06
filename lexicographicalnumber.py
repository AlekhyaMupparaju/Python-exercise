n=int(raw_input())
a=[]
for i in range(0,n):
    b=int(raw_input())
    a.append(b)
a.sort()
print str(a).replace('[','').replace(']','').replace(',','').replace(' ','')
