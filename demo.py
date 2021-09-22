import pyodbc
import json
import collections
import pyqrcode
import png



strsql =" select top 10 code from (select distinct code  from thaiplantdict where code <>'' ) as a "

print(strsql);

connstr = 'DRIVER={SQL Server};SERVER=(local)\sql2008;UID=usr;PWD=usr;DATABASE=mplant;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
cursor.execute(strsql)
print('ok')

rows = cursor.fetchall()

#print(rows)
items=[]
for row in rows:
    print(row.code )
    url = pyqrcode.create(row.code )
    url.png('qrapp/'+row.code +'.png', scale=7)
    #row.itemid
conn.close()

