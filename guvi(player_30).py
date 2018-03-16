s=raw_input()
r=raw_input()
k=int(raw_input())
count=0
if len(s)==len(r):
    for i in range(len(s)):
        if s[i]!=r[i]:
            count=count+1
if k==count:
    print "YES"
else:
    print "NO"
