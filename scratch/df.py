import pandas as pd
from openpyxl import load_workbook
la='E:\\gru module\\billing software\\BILL DATABASE.xlsx'
bill_save=pd.read_excel(la,sheet_name='Sheet1')
l=[[1, 'hhh', 444.0], [2, 'kk', 44.0], [3, ';;;', 44.0], [4, 'hhh', 555.0]]
a=[a[0] for a in l]
b=[a[1] for a in l]
c=[a[2] for a in l]
t=pd.DataFrame({"SNO":a,"SAREENO":b,"PRICE":c})
o=pd.ExcelFile.parse(,sheet_name="Sheet1")
print(o)

print(a,b,c)
pd.set_option('display.max_rows', 220,"display.max_column",100)

print()