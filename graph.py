import matplotlib.pyplot as pt
"""x=[1,2,3]
y=[2,4,1]

pt.plot(x,y)
pt.xlabel('X-axis')
pt.ylabel('Y-axis')
pt.title('my first graph...!')
pt.show()"""

"""x=[1,2,3,4,5]
y=[78,89,83,93,87]
x1=[1,2,3,4,5]
y1=[87,80,75,90,93]
pt.plot(x,y,label="upasana",marker='o',ms=10,mec='green',mfc='red')
pt.plot(x1,y1,label="piyu",marker='*',ms=20,mec='yellow',mfc='black')
pt.xlabel('semester-1')
pt.ylabel('percentage')
pt.title('two line')
pt.legend()
pt.show()"""

"""x=[2,3,4,2,4,2]
y=[2,5,2,4,4,2]
pt.plot(x,y)
pt.xlim(0,8)
pt.ylim(0,8)
pt.xlabel('x-axis')
pt.ylabel('y-axis')
pt.title('star')
pt.show()"""


"""x=[1,2,3,4,5]
y=[60,80,75,90,88]
x1=[1,2,3,4,5]
y1=[70,80,70,85,90]
x2=[1,2,3,4,5]
y2=[80,85,80,80,80]
pt.plot(x,y,label="upasana",c='r',ls='--',lw=2)
pt.plot(x1,y1,label="trisha",c='b',ls=':',lw=2)
pt.plot(x2,y2,label="viha")

pt.xlabel('semester')
pt.ylabel('percentage')
pt.title('data')
pt.legend()
pt.show()"""



x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,7,6,8,9,11,12,12]
y1=[1,4,4,7,8,10,11,13,15,16]
pt.scatter(x,y,label="stars",color="blue",marker="*",s=30)
pt.scatter(x,y1,label="plus",color="red",marker="+",s=30)
pt.scatter(y,y1,label="triangle",color="green",marker="^",s=30)
pt.xlabel('x-axis')
pt.ylabel('y-axis')
pt.legend()
pt.title('scatter!!!')
pt.show()

"""x=[1,2,3,4,5,6]
height=[10,24,36,40,8,24]
x_label=['one','two','three','four','five','six']
pt.bar(x,height,tick_label=x_label,width=0.5,color=["blue","red"])
pt.xlabel('x-axis')
pt.ylabel('y-axis')
pt.title('bar chart ex')
pt.show()"""

"""x=[23,17,29,35,12]
lang=['c','c++','PHP','JAVA','PYTHON']
c=['m','y','b','r','g']
pt.pie(x,labels=lang,colors=c,startangle=0,shadow=False,autopct='%.2f%%',explode=(0.1,0,0,0,0),radius=1.0,counterclock=True,pctdistance=0.7,labeldistance=1.1)
pt.title("pie chart!!!")
pt.show()"""
