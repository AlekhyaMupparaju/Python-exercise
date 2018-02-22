s=raw_input()
c=len(s)
s=list(s)
if c%2 ==0:
    
    for i in range(0,c,2):
        t=s[i]
        s[i]=s[i+1]
        s[i+1]=t
    print "".join(s)
else:
    print "Give even string"
