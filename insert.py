import mysql.connector
from tkinter import *
from tkinter import messagebox

def hello():
    rollno=e1.get()
    name=e2.get()
    stream=e3.get()
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bca6')
    mycursor=mydb.cursor()
    sql="INSERT INTO student VALUES(%s,%s,%s)"
    data=(rollno,name,stream)
    mycursor.execute(sql,data)
    mydb.commit()
    messagebox.showinfo("","record inserted successfully")

w=Tk()
w.geometry("500x500+100+100")

l1=Label(w,text="insert record",font=('Arial',25)).place(x=150,y=20)
l2=Label(w,text="roll no").place(x=100,y=100)
l3=Label(w,text="name").place(x=100,y=150)
l4=Label(w,text="stream").place(x=100,y=200)

e1=Entry(w,width=20)
e1.place(x=200,y=100)
e2=Entry(w,width=20)
e2.place(x=200,y=150)
e3=Entry(w,width=20)
e3.place(x=200,y=200)

b1=Button(w,text="insert",command=hello,height=2,width=20)
b1.place(x=150,y=340)
w.mainloop()
    
