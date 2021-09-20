import pyodbc
import json
import collections
import pyqrcode
import png



strsql =' select top 100 z.itemid ,rtrim(ltrim(a.FPDLINE)) as lineid '
strsql = strsql + ' from ( '
strsql = strsql + ' select distinct itemid from lottracking.dbo.LotProduction with(nolock) '
strsql = strsql + ' where year(LotMFDate) = 2019 '
strsql = strsql + ' ) as z ,taiyo.dbo.SD05PDDS  a with(nolock) '
strsql = strsql + ' where len(z.itemid)>=7 '
strsql = strsql + ' and z.itemid=a.FPDCODE '
strsql = strsql + " and a.FPDLINE='101' "

print(strsql);

connstr = 'DRIVER={SQL Server};SERVER=200.200.200.1;UID=xxxxx;PWD=xxxx;DATABASE=lottracking;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
cursor.execute(strsql)
print('ok')

rows = cursor.fetchall()

#print(rows)
items=[]
for row in rows:
    print(row.itemid)
    print(row.itemid)
    url = pyqrcode.create(row.itemid)
    url.png('file/'+row.lineid+'/'+row.itemid +'.png', scale=2)
    #row.itemid
conn.close()

