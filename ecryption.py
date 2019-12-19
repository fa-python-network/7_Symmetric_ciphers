msg='Hello! How are you? What are you doing?'
k=input('Sdvig na k=')


def encrypt(msg,k):  
    m=''
    
    for i in msg:
        m+=(chr(((ord(i)+k)%256)))
    
    return m

dsmg=encrypt(msg,k)
print('Encrypt: '+ dsmg)



def decrypt(k,dmsg):
    d=''
    for i in dmsg:
        d+=(chr(((ord(i)-k)%256)))
        #print(chr(((ord(i)-k)%256)))
    return d

ms=decrypt(k,dsmg)
print('Decrypt: '+ ms)


def finder(m):
    d={}
    for i in m:
        if ord(i) in d:
            d[ord(i)]+=1
        else:
            d[ord(i)]=1
    
    max=0
    maxch='-'
    for i in d.items():
        if i[1]>max:
            max=i[1]
            maxch=i[0]
    l=maxch-32
    return l

    

n=finder(dsmg)
print('We found k! k= ' +str(n))
dg=decrypt(n,dsmg)


print('Decrypt with found k: '+dg)

