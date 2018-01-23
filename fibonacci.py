n=-1
m=1
x=int(raw_input())
for i in range(x):
    t=n+m
    n=m
    m=t
    print t,
