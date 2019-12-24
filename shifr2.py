s1=str(input("enter the string:"))
str1=[]
str4=[]
r = 5
for s in s1:
	str1.append(ord(s)+r)
k1=0
i1=0
for i in str1:
    k=str1.count(i)
    if (k>k1):
    	k1=k
    	i1=i
print(k1,i1)
prob=ord(' ')
#print("prob=",prob)
r2=i1-prob
#str4=[]
for s in str1:

    a1=chr(s-r2)
    str4.append(a1)
print(''.join(str4))
