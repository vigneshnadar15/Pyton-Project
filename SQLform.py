from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from PIL import *
import io
import base64


con = mysql.connector.connect(host='127.0.0.1', user='root', password='admin', database='vignesh')
cusor = con.cursor()
top = Tk()
top.geometry("500x500")
ida = IntVar()
name = StringVar()
city = StringVar()
sal = IntVar()
path = StringVar()
global pic
pic = Label(top)
pic.place(x=360, y=22)



def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def addx():
    try:
        binary_data = convertToBinaryData(path.get())
        #encoded_data = base64.b64encode(binary_data).decode('utf-8')
        sql = "INSERT INTO EMP VALUES (%s, %s, %s, %s, %s)"
        data = (ida.get(), name.get(), city.get(), sal.get(), binary_data)
        cusor.execute(sql, data)
        con.commit()
        ida.set("")
        name.set("")
        city.set("")
        sal.set("")
        path.set("")
    except mysql.connector.errors.IntegrityError:
        messagebox.showerror("ERROR", "There is already an employee with the specified ID")
    except FileNotFoundError:
         messagebox.showerror("ERROR", "Enter the image path")


def deletex():
    sql = "DELETE FROM emp WHERE eid=" + str(ida.get()) + ";"
    cusor.execute(sql)
    con.commit()
    ida.set("")
    name.set("")
    city.set("")
    sal.set("")

def searchx():
    try:
        sql = "SELECT ida, name, city, sal FROM EMP WHERE ida=" + str(ida.get()) + ";"
        cusor.execute(sql)
        res = cusor.fetchall()
        query = "SELECT img FROM EMP WHERE ida=" + str(ida.get()) + ";"
        cusor.execute(query)
        blob_data = cusor.fetchone()[0]
        if blob_data==None:
             messagebox.showerror("ERROR", "There is no picture for the specified ID")
        else:
             image1 = Image.open(io.BytesIO(blob_data))
             width, height=200,200
             image1 = image1.resize((width, height), Image.ANTIALIAS)
             img = ImageTk.PhotoImage(image1)
             pic.config(image=img)
             pic.image = img
        for EMP in res:
            ida.set(EMP[0])
            name.set(EMP[1])
            city.set(EMP[2])
            sal.set(EMP[3])
    except UnboundLocalError:
        messagebox.showerror("ERROR", "There is no details for the specified ID")
    except TypeError:
         messagebox.showerror("ERROR", "There is no details for the specified ID")

def updatex():
    sql = "UPDATE EMP SET name = '" + name.get() + "', City = '" + city.get() + "', Sal = '" + str(sal.get()) + "' WHERE ida = " + str(ida.get()) + " ;"
    cusor.execute(sql)
    con.commit()

def lastx():
    try:
         sql = "SELECT * FROM EMP ORDER BY ida DESC LIMIT 1;"
         cusor.execute(sql)
         res = cusor.fetchall()
         for EMP in res:
              ida.set(EMP[0])
              name.set(EMP[1])
              city.set(EMP[2])
              sal.set(EMP[3])
         query = "SELECT img FROM EMP ORDER BY ida DESC LIMIT 1;"
         cusor.execute(query)
         blob_data1 = cusor.fetchone()[0]
         if blob_data1==None:
              messagebox.showerror("ERROR", "There is no picture for the specified ID")
              pic.config(image='')
              pic.image = img
         else:
              image1 = Image.open(io.BytesIO(blob_data1))
              img = ImageTk.PhotoImage(image1)
              pic.config(image=img)
              pic.image = img
    except TypeError:
         messagebox.showerror("ERROR", "hello  There is no details for the specified ID")

def prevx():
    sql = "SELECT * FROM EMP WHERE ida=" + str(ida.get() - 1) + ";"
    cusor.execute(sql)
    res = cusor.fetchall()
    for EMP in res:
        ida.set(EMP[0])
        name.set(EMP[1])
        city.set(EMP[2])
        sal.set(EMP[3])
        blob_data2 = EMP[4]
          #query = "SELECT img FROM EMP WHERE ida=" + int(ida.get()-1) + ";"
         # cusor.execute(query)
    #cusor.fetchone()
    if blob_data2=='':  #None
        messagebox.showerror("ERROR", "There is no picture for the specified ID")
    else:
        image1 = Image.open(io.BytesIO(blob_data2))
        img = ImageTk.PhotoImage(image1)
        pic.config(image=img)
        pic.image = img

def nextx():
    sql = "SELECT * FROM EMP WHERE ida=" + str(ida.get() + 1) + ";"
    cusor.execute(sql)
    res = cusor.fetchall()
    for EMP in res:
        ida.set(EMP[0])
        name.set(EMP[1])
        city.set(EMP[2])
        sal.set(EMP[3])
    #query = "SELECT img FROM EMP WHERE ida=" + str(ida.get()+1) + ";"
    #cusor.execute(query)
    blob_data3 = EMP[4]#cusor.fetchone()
    if blob_data3==None:
         messagebox.showerror("ERROR", "There is no picture for the specified ID")
    else:
         image1 = Image.open(io.BytesIO(blob_data3))
         img = ImageTk.PhotoImage(image1)
         pic.config(image=img)
         pic.image = img

def firstx():
    sql = "SELECT * FROM EMP LIMIT 1;"
    cusor.execute(sql)
    res = cusor.fetchall()
    for EMP in res:
        ida.set(EMP[0])
        name.set(EMP[1])
        city.set(EMP[2])
        sal.set(EMP[3])
    query = "SELECT img FROM EMP limit 1;"
    cusor.execute(query)
    blob_data4 = cusor.fetchone()[0]
    if blob_data4==None:
         pic.config(image='')
         messagebox.showerror("ERROR", "There is no picture for the specified ID")
         
         
    else:
         image1 = Image.open(io.BytesIO(blob_data4))
         #pic = Label(top)
         #pic.place(x=360, y=22)
         img = ImageTk.PhotoImage(image1)
         pic.config(image=img)
         pic.image = img

l1 = Label(top, text="SQL form", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9, 'bold')).place(x=230, y=5)
l2 = Label(top, text="ID", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9, 'bold')).place(x=150, y=30)
l3 = Label(top, text="Name", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9)).place(x=150, y=60)
l4 = Label(top, text="City", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9)).place(x=150, y=90)
l5 = Label(top, text="Salary", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9)).place(x=150, y=120)
l6 = Label(top, text="Photo path", bg='#83838B', width=8, fg='#FFFFF5', font=('Helvetica bold', 9)).place(x=150, y=150)

e1 = Entry(top, textvariable=ida).place(x=230, y=30)
e2 = Entry(top, textvariable=name).place(x=230, y=60)
e3 = Entry(top, textvariable=city).place(x=230, y=90)
e4 = Entry(top, textvariable=sal).place(x=230, y=120)
e5 = Entry(top, textvariable=path).place(x=230, y=150)

b1 = Button(top, text="ADD", width=6, command=addx).place(x=150, y=180)
b2 = Button(top, text="DELETE", width=6, command=deletex).place(x=150, y=210)
b3 = Button(top, text="SEARCH", width=6, command=searchx).place(x=150, y=240)
b4 = Button(top, text="Update", width=6, command=updatex).place(x=150, y=270)
b5 = Button(top, text="PREV", width=6, command=prevx).place(x=250, y=180)
b6 = Button(top, text="NEXT", width=6, command=nextx).place(x=250, y=210)
b7 = Button(top, text="<<", width=6, command=firstx).place(x=250, y=240)
b8 = Button(top, text=">>", width=6, command=lastx).place(x=250, y=270)

top.mainloop()
