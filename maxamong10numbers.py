number=[]
n=int(raw_input("Enter number of elements:"))
for i in range(0,n):
    b=int(raw_input())
    number.append(b)
number.sort()
print(number[n-1])
