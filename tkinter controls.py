from tkinter import *
from tkinter import messagebox
w= Tk()
w.geometry("700x400+500+200")

#label
"""l1=Label(w,text="hello",bg="blue",fg="red")
l1.place(x=100,y=10)

l2=Label(w,text="hello",bg="blue",width=10)
l2.place(x=100,y=50)

l3=Label(w,text="this is tkinter label",wraplength=50)
l3.place(x=100,y=100)

l4=Label(w,text="tkinter",underline=2,bg="red",font=("times","20","bold"))
l4.place(x=100,y=150)"""



#entry box
"""e1=Entry(w,fg="blue",bg="yellow").place(x=80,y=50)
e2=Entry(w,bg="red",width=30,justify="right").place(x=80,y=90)
e3=Entry(w,show="*",bd=5).place(x=80,y=130)
e4=Entry(w,selectforeground="blue",selectborder=5,selectbackground="yellow").place(x=80,y=170)
e5=Entry(w,cursor="dot").place(x=80,y=210)"""

#button
"""w.title("button widget example")
def click():
    messagebox.showinfo("hello","button 4 clicked")
def go():
    t=e1.get()
    messagebox.showinfo("title",t)
btn1=Button(w,text="submit",activebackground="red").place(x=30,y=170)
btn2=Button(w,text="cancel",activeforeground="blue").place(x=100,y=170)
btn3=Button(w,text="Disable",state="disable").place(x=170,y=170)
btn4=Button(w,text="click me",command=click).place(x=240,y=170)
e1=Entry(w)
e1.place(x=50,y=120)

btn5=Button(w,text="button5",bd=5,command=go,height=5,width=10).place(x=310,y=170)"""
#checkbutton
"""def hello():
    messagebox.showinfo("","you select basketball")

c1=Checkbutton(w,text="cricket",selectcolor="yellow",activebackground="red")
c1.place(x=100,y=100)
c2=Checkbutton(w,text="football",fg="blue",activeforeground="red")
c2.place(x=100,y=130)
c3=Checkbutton(w,text="carrom",state="disable")
c3.place(x=100,y=160)
c4=Checkbutton(w,text="basketball",command=hello)
c4.place(x=100,y=190)"""

#radiobutton
"""def hello():
    if v.get()==1:
        messagebox.showinfo("","you selected male option")
    else:
        messagebox.showinfo("","you selected female option")
v=IntVar()

l1=Label(w,text="gender").place(x=50,y=100)
r1=Radiobutton(w,text="male",command=hello,value=1,variable=v)
r1.place(x=100,y=100)
r2=Radiobutton(w,text="female",command=hello,value=2,variable=v)
r2.place(x=100,y=150)"""

#listbox
"""l1=Label(w,text="programming language")
l=Listbox(w)
l.insert(0,"python")
l.insert(1,"java")
l.insert(2,"c++")
l.insert(3,"adv python")
l.insert(4,"c")
l1.place(x=50,y=100)
l.place(x=200,y=100)
l.selection_set(2)
print(l.size())"""

#spinbox
"""s1=Spinbox(w,from_=1,to=31,increment=2,fg="navyblue")
s1.place(x=50,y=130)
months=["january","february","march","april","may","june","july","august","september","october","november","december"]
s2=Spinbox(w,values=months,wrap=True)
s2.place(x=200,y=130)
s3=Spinbox(w,from_=1990,to=2024)
s3.place(x=350,y=130)"""

#message
"""l1=Label(w,text="message",font="70",fg="navyblue")
l1.place(x=100,y=100)

mgs=Message(w,text="this is a message for you...",width=200)
mgs.place(x=180,y=100)"""

#messagebox
"""def hello():
    messagebox.showinfo("title","hello")
    messagebox.showwarning("","this is warning")
    messagebox.askquestion("","are you sure")
    messagebox.askretrycancel("","wann try againn")
    messagebox.showerror("","error")

btn=Button(w,text="click",command=hello)
btn.place(x=100,y=100)"""

#textbox
"""l1=Label(w,text="address")
l1.place(x=70,y=10)
t1=Text(w,height=5,width=25,spacing1=2)
t1.place(x=160,y=10)
b1=Button(w,text="close",command=w.destroy)
b1.place(x=200,y=150)"""

#scale
"""s1=Scale(w,from_=1,to=100,orient=HORIZONTAL)
s1.place(x=100,y=100)
s2=Scale(w,troughcolor="red",from_=1,to=100,orient=HORIZONTAL)
s2.place(x=100,y=200)
s3=Scale(w,troughcolor="blue",from_=51,to=150,orient=VERTICAL)
s3.place(x=250,y=100)"""

#frame
"""f1=Frame(w,width=150,height=150,bg="navyblue")
f1.place(x=10,y=10)

b1=Button(f1,text="block1")
b1.place(x=10,y=10)

b2=Button(f1,text="block2")
b2.place(x=10,y=30)

b3=Button(f1,text="block3")
b3.place(x=10,y=50)

f2=Frame(w,width=100,height=100,bg="orange",cursor="dot")
f2.place(x=100,y=200)

b4=Button(f2,text="block4")
b4.place(x=10,y=10)

b5=Button(f2,text="block5")
b5.place(x=10,y=30)"""

#canvas
"""c1=Canvas(w,width=680,height=530,bg="black")
c1.place(x=10,y=10)

line=c1.create_line(400,400,600,400,fill="green",width="3")
coord=10,10,300,300

arc1=c1.create_arc(coord,start=0,extent=150,fill="pink")
arc2=c1.create_arc(coord,start=150,extent=210,fill="blue")
oval1=c1.create_oval(400,10,600,300,fill="yellow")
poly=c1.create_polygon([250,300,350,400,250,500,150,400],outline="gray",fill="red",width=2)"""

#scrollbar(vertical)
"""l1=Listbox(w,width=30,height=20)
l1.pack(side="left")

sb=Scrollbar(w,orient="vertical",command=l1.yview)
sb.pack(side="right",fill="y")

l1.config(yscrollcommand=sb.set)
for no in range(100):
    no1=no+1
    l1.insert(no,"value"+str(no1))"""

#scrollbar(horizantal)
"""l1=Listbox(w,width=30,height=20)
l1.pack(side="top")
l1.insert(0,"hello hello  gello python............................................")
sb=Scrollbar(w,orient="horizontal",command=l1.xview)
sb.pack(side="bottom",fill="x")


l1.config(xscrollcommand=sb.set)"""
menubar=Menu(w)
w.config(menu=menubar)
file_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_separator()
sub_menu=Menu(file_menu,tearoff=0)
file_menu.add_cascade(label="save",menu=sub_menu)
sub_menu.add_command(label="save")
sub_menu.add_command(label="save as")
file_menu.add_separator()
file_menu.add_command(label="exit",command=w.destroy)
edit_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="undo")
edit_menu.add_command(label="redo")
edit_menu.add_separator()
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")
help_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="help",menu=help_menu)
help_menu.add_command(label="welcome")
help_menu.add_command(label="about")
w.mainloop()


