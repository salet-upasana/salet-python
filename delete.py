import mysql.connector
from tkinter import *
from tkinter import messagebox

def hello():
    rollno=e1.get()
   
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bca6')
    mycursor=mydb.cursor()
    sql="DELETE FROM student WHERE rollno='%s'"
    mycursor.execute(sql,(rollno))
    mydb.commit()
    messagebox.showinfo("","record deleted successfully")

w=Tk()
w.geometry("500x500+100+100")

l1=Label(w,text="delete record",font=('Arial',25)).place(x=150,y=20)
l2=Label(w,text="roll no").place(x=100,y=100)


e1=Entry(w,width=20)
e1.place(x=200,y=100)


b1=Button(w,text="delete",command=hello,height=2,width=20)
b1.place(x=150,y=150)
w.mainloop()
    
