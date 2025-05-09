import mysql.connector
from tkinter import *

#entry
"""def hello():
    
   mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bca6')
   mycursor=mydb.cursor()
   mycursor.execute("SELECT * FROM student")
   i=1
   for std in mycursor:
       for j in range(len(std)):
           e=Entry(w,width=10,fg="blue")
           e.grid(row=i,column=j)
           e.insert(END,std[j])
           e.config(state='readonly')
       i=i+1
  

        

w=Tk()
w.geometry("500x250")
l1=Label(w,width=10,text="id").grid(row=0,column=0)
l2=Label(w,width=10,text="name").grid(row=0,column=1)
l3=Label(w,width=10,text="stream").grid(row=0,column=2)

b1=Button(w,text="display",command=hello,height=2,width=15)
b1.place(x=300,y=100)
w.mainloop()"""

#label
def hello():
    
   mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bca6')
   mycursor=mydb.cursor()
   mycursor.execute("SELECT * FROM student")
   i=1
   for std in mycursor:
       for j in range(len(std)):
           l=Label(w,width=10,text=std[j],fg="blue")
           l.grid(row=i,column=j)
           
       i=i+1
  

        

w=Tk()
w.geometry("500x250")
l1=Label(w,width=10,text="id").grid(row=0,column=0)
l2=Label(w,width=10,text="name").grid(row=0,column=1)
l3=Label(w,width=10,text="stream").grid(row=0,column=2)

b1=Button(w,text="display",command=hello,height=2,width=15)
b1.place(x=300,y=100)
w.mainloop()


