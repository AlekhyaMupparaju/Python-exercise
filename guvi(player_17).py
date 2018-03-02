n=int(raw_input())
m=int(raw_input())
i=1
while (n and m)>0:
    if ((i%n == 0) and (i%m == 0)):
        print i
        break
    i=i+1
