import pyodbc
import json
import collections
import pyqrcode
import png



strsql =" select distinct code  from thaiplantdict where code <>''  "

print(strsql);

connstr = 'DRIVER={SQL Server};SERVER=(local)\sql2008;UID=usr;PWD=usr;DATABASE=mplant;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
cursor.execute(strsql)


rows = cursor.fetchall()

#print(rows)
items=[]
for row in rows:
    print(row.code )

    # url = pyqrcode.create(row.code )    
    # url.png('qrapp/'+row.code +'.png', scale=7)
    
    url = pyqrcode.create('https://www.dnp.go.th/botany/mplant/word.html?code=' +row.code )    
    url.png('qrlink/'+row.code +'.png', scale=7)
    
conn.close()
print('ok')

