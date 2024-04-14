def changelist(l,s,a):
    p=l[s:a+1]
    p=p[::-1]
    l[s:a+1]=p
    return l

print(changelist([1,2,3,4,5,6,7,8,9],0,3))

