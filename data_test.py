import pandas as pd
import matplotlib.pyplot as plt
t="E:\data\student\student-mat.csv"
b='E:\data\student\student-por.csv'
i="E:\data\Forest\lfire.csv"
hh="E:\data\QCM Sensor Alcohol Dataset\QCM10.csv"
w="k.xlsx"
k=pd.read_excel(w,sheet_name="Daily Sales")
i=pd.read_csv(i,sep=",")
l=i.head(10)
S={'X':7,'Y':4,'month' :'aug','day': 'mon','FFMC':86,'DMC':88.0 ,"DC":94.3,'ISI':14.7,'temp':18.0  ,'RH':33,  "wind":6.7 , "rain":0.2 , 'area':0.0}

print(l)
x=list()
for g in l["X"]:
    x.append(g)
y=list()
for g in l["Y"]:
    y.append(g)
plt.plot(x,y)
plt.show()
pd.set_option('display.max_rows', 220,"display.max_column",100)


