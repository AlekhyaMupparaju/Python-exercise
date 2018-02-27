s1=raw_input()
s2=raw_input()
l1=len(s1)
l2=len(s2)
count=0
if l1==l2:
    for i in range(l1):
        if s1[i]!=s2[i]:
            count=count+1
            
else:
    print "No"
if count==1:
    print "Yes"
else:
    print "No"
