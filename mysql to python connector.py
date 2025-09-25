import mysql.connector as ms

con=ms.connect(user='root',password='Mysql@1234',\
         host='localhost',database='vcube')
print(con) 
con.close()
