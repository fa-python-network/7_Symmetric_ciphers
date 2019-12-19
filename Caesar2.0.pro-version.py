msg='mama lu l'
k=int(input('k='))

def encode(msg,k):
    d=''
    str=msg
    m=str.split()
    for i in m:
        c=len(i)
        k1=k+c
        for a in i:
            d+=(chr(((ord(a)+k1)%256)))
        d+=chr(32)
    return d

dg=encode(msg,k)
print(dg)


def decode(dmsg,k):
    stroka=''
    st=''
    d=''
    for i in dmsg:
        if ord(i)!=(32+k):
            st+=i
            
        else:
            st+=' '

    m=st.split()
    #print(m)
    for i in m:
        c=len(i)
        k1=k+c
        for a in i:
            d+=(chr(((ord(a)-k1)%256)))
        d+=chr(32)
    return d
    
        
    #return stroka

#newstroka=decode(dg)
print(decode(dg,k))
    
    





#def decode(msg,k):