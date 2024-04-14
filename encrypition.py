def int_enc(i):
    l=[chr(a) for a in range (2000,1990,-1)]
    k=[int(a) for a in str(i)]
    st=str()
    for a in range (len(k)):
        h=k[a]
        st+=l[h]
    return st

def str_enc(i):
    u=[a for a in "abcdefghijklmnopqrstuvwxyz"]+[" ",",",".",";"]
    s=[chr(a) for a in range(2031,2001,-1)]
    k=[a.lower() for a in i]
    st=str()
    for a in range (len(k)):
       h=u.index(k[a])
       st+=s[h]
    return st
def rev_str_enc(sr):
    u=[a for a in "abcdefghijklmnopqrstuvwxyz"]+[" ",",",".",";"]
    s=[chr(a) for a in range(2031,2001,-1)]
    k=[a.lower() for a in sr]
    p=str()
    for a in range (len(k)):
        h=s.index(k[a])
        p+=u[h]
    return p
def rev_int_enc(sr):
    l=[chr(a) for a in range (2000,1990,-1)]
    k=[a for a in str(sr)]
    hu=[int(a) for a in range(10)]
    st=str()
    for a in range (len(k)):
        h=l.index(k[a])
        st+=str(h)
    return st
if __name__=="__main__":
    for a in "abcdefghijklmnopqrstuvwxyz":
        print(a,str_enc(a))
        print()
    for a in range(10):
        print(a,int_enc(a))
        print()
while True:
    i=input()
    try:
        print(str_enc(i))
    except:
        print(int_enc(i))
    i=str()
