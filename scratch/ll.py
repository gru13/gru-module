import pandas as pd
def chck(a,d):
    for i in range(len(d)+1):
        if a == d[i]:
            return d[i]
def jj(a,y):
    o=[]
    for i in range(len(a)):
        u=[a[i],y[i]]
        o.append(u)
    return o
def k (o,l):
    y=[]
    for i in o[l]:
        y.append(i)
    return y
forest_fire={"X":[2,5,6,8,9,9,7,7],
             "Y":[2,2,5,5,5,8,9,3],
             "temp":[55.2,54.5,53.9,51,54.3,55.2,54.5,51.9],
             "humidity":[0.20,0.30,0.66,0.5,0.02,0.14,0.96,0.74],
             "area":[200,300,500,400,940,900,100,600],
             }
ff=pd.DataFrame(forest_fire)
t={"X":6,"Y":5,"temp":55.2,"humidity":0.3,"area":None}
ff=ff.append(t,ignore_index=True)
x=chck(t["X"],ff["X"])
y=chck(t["Y"],ff["Y"])
u=[t["X"],t["Y"]]
i=k(ff,"X")
j=k(ff,"Y")
e=jj(i, j)
if u in e :
    print


