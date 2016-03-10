
#python querydatabase
from os import getenv


import pypyodbc
print ("Hello World DB test program")

conn = pypyodbc.connect(
    'Driver={SQL Server};'
    'server=ELITELEADRRSPC;'
    'Database=MATHWIRE;'
    'uid=boomer;pwd=glock45bangbang@1980'
    )

cursor= conn.cursor() 
SQLCommand= ("SELECT  FirstName, LastName ""FROM BasicInfo" )
cursor.execute(SQLCommand)
results=cursor.fetchone()
print(results[0],results[1])


conn.close()