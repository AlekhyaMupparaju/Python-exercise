a=int(raw_input())
b=[]
while a!=0:
    c=a%10
    if c%2==1:
        b.append(c)
    a=a/10
print str(b[::-1]).replace('[',"").replace(']',"")
