from collections import Counter
s1=str(input("enter the string:"))
str1=[]
str2=[]
str3=[]
r = 5
for s in s1:
	str1.append(ord(s)+r)

for s in str1:
    a=chr(s)
    str3.append(a)

print(str1)
print(''.join(str3))
for s in str1:
    a=s-r
    a1=chr(a)
    str2.append(a1)
print(''.join(str2))

