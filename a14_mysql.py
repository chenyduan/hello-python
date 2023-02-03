

import MySQLdb

# todo
db = MySQLdb.connect()

cursor = db.cursor()
print("执行sql")
cursor.execute("select version()")
data = cursor.fetchone()
print(data)


# 关闭连接
db.close()