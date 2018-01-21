def ispoweroftwo(n):
    n=n/2.0
    if n==2:
        return True
    elif n>2:
        return ispoweroftwo(n)
    else:
        return False
n=int(raw_input())
if ispoweroftwo(n):
    print "Yes"
else:
    print "No"
