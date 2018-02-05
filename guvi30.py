h1=int(raw_input())
m1=int(raw_input())
h2=int(raw_input())
m2=int(raw_input())
h=h1-h2
m=m1-m2
if h<0:
    h=-h
if m<0:
    m=-m
print h,":",m
