'''
def marsExploration(s):
    s=s.lower()
    l=len(s)
    sa=list( a for a in s)
    h=sa.count('s')
    i=sa.count('o')
    c=int(l/3)
    if c*2==h or c==i:
        print(0)
    else:
        g=(c*2)-h
        print(g)'''

def marsExploration(s):
    n=3
    dive=[s[i:i+n]for i in range(0, len(s), n)]
    n=dive.count('SOS')
    for a in range(n):
        dive.remove('SOS')
    l=str()
    for a in dive:
        l+=a
    dive=[a for a in l]
    for a in range(dive.count('S')):
        dive.remove('S')
    for a in range(dive.count('O')):
        dive.remove('O')
    return len(dive)
marsExploration("SOSOSOSOSDSDSKWOSDOSDOASDOASDFAFJDFDOSOSOWNSOSOSNDSKDDOSOSOSJDSDSOOSOSDSDOSASSOASDSAOSOSODSDSOASDWS")

