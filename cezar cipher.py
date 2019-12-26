def encrypt(key, str):
    sp1=[]
    sp2=[]
    for i in str:
        sp1.append((ord(i)+key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    cipher=''.join(sp2)   
    return cipher 

def decrypt(key, cipher):
    sp1=[]
    sp2=[]
    for i in cipher:
        sp1.append((ord(i)-key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    str=''.join(sp2)   
    return str

def hack(cipher):
    num=[]
    for i in range(len(cipher)):
        num.append([cipher.count(cipher[i]),cipher[i]])
        max=0
        for j in range(len(num)):
            if num[j][0] > max:
                max=num[j][0]
                elmax=num[j][1]
    key=ord(elmax)-ord(' ')%256
    sp1=[]
    sp2=[]
    for i in cipher:
        sp1.append((ord(i)-key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    str=''.join(sp2)   
    return str

msg = "Koroteev is the epitomy of discipline "
k = int(input("input key: "))
rez = encrypt(k,msg)
sh = decrypt(k,rez)
print(sh, "-> decoded")
print(rez, "-> encoded")



sen = input("input the encrypted sentence: ")
r = hack(sen)
print("decryption: ", r)
