s=raw_input()
c=len(s)
newstr=s
vowels=('a','e','i','o','u')
for j in range(c):
    for i in s.lower():
        if i in vowels:
            newstr=newstr.replace(i,"")
print newstr[::-1]
