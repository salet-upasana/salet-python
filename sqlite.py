import sqlite3
#print("connection successfully")
conn=sqlite3.connect("college2025.db")
#print("database create successfully")
'''conn.execute("CREATE TABLE student(roll_no INTEGER ,name TEXT,stream TEXT)")
print("create table successfully")'''
'''conn.execute("INSERT INTO student VALUES(5,'tapu','bsw')")
conn.commit()
print("records inserted successfully")'''
'''conn.execute("UPDATE student SET  name='viha' where roll_no=1")
conn.commit()
print("records update successfully")'''
'''conn.execute("DELETE FROM student where roll_no=1")
conn.commit()
print("records delete successfully")'''
cursor=conn.execute("SELECT * FROM student" )
myresult=cursor.fetchall()
for x in myresult:
    print(x)

