s=raw_input()
count1=0
count2=0
for i in range(len(s)):
    if '('==s[i]:
        count1=count1+1
    elif ')'==s[i]:
        count2=count2+1
if count1==count2:
    print "YES"
else:
    print "NO"
