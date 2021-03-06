from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from pymysql import OperationalError
import datetime
import os
import time
from tkinter import ttk
now = datetime.datetime.utcnow()


#connecting to the database
try:


    db = pymysql.connect(host="localhost",user="root",passwd="",database="LifechoicesOnline")
    global mycur
    mycur = db.cursor()

except OperationalError as OperationalError:

    messagebox.showerror("An operational error has occured as:", {OperationalError})

finally:
    messagebox.Message("Successfully created a connection with MySQL database Server")






def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("400x400")
    Label(succ, text="Registration successful...", fg="green", font=("Arial",12,"bold")).pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    """this functions will allow the admin of the system to add new ussers"""
    fullname_info = fullname.get()
    username_info = username.get()
    password_info = password.get()
    cellphone_info=cell_phone.get()

    Date = now.strftime("%Y-%m-%d %H:%M")

    if username_info == "":
        error()
    elif password_info == "":
                error()

    elif fullname_info == "":
        error()

    elif Date =="":
        error()
    else:
        sql = "insert into users values(%s,%s,%s,%s,%s)"
        t = (fullname_info,username_info, password_info,cellphone_info,Date)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("650x650+0+0")
    root1.configure(background="powder blue")
    global username
    global password
    global fullname
    global cell_phone

    Label(root1,text="Register your account",bg="cadetblue",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    fullname = StringVar()
    cell_phone=StringVar()

    Label(root1, text="").pack()
    Label(root1,text="FullName").pack()
    Entry(root1,textvariable=fullname).pack()


    Label(root1,text="").pack()
    Label(root1,text="Username",font="bold").pack()
    Entry(root1,textvariable=username).pack()

    Label(root1, text="").pack()
    Label(root1, text="Password").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()

    Label(root1, text="").pack()
    Label(root1,text=" Mobile Number").pack()
    Entry(root1,textvariable=cell_phone).pack()


    Button(root1,text="Register",bg="green2",command=register_user).pack()

def login():

    """this function verifies if the information in
    the table users is correct and they can log in """
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.configure(background="steelblue")
    root2.geometry("500x500")
    global fullname_verify
    global username_varify
    global password_varify
    global cellphone_verify

    Label(root2, text="Log-In Portal", bg="cadetblue", fg="black", font=("Arial",12,"bold"),width=300).pack()

    fullname_verify =StringVar()
    username_varify = StringVar()
    password_varify = StringVar()
    cellphone_verify =StringVar()


    Label(root2,text="").pack()
    Label(root2, text="FullName").pack()
    Entry(root2,textvariable=fullname_verify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Username", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()

    Label(root2, text="Password").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()

    Label(root2,text="MobileNumber").pack()
    Entry(root2,textvariable=cellphone_verify).pack()
    Label(root2,text="").pack()
    Button(root2, text="Log-In", bg="green2",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    """this UI component only gets called when the user log in,
    """
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("350x350")
    Label(logg, text="Login Successfull! Enjoy Your Day {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()
    db = pymysql.connect(host="localhost", user="root", passwd="", database="LifechoicesOnline")
    # global mycur
    mycur = db.cursor()
    DateTime = now.strftime("%Y-%m-%d %H:%M")
    sql = "insert  fullname=%s, username=%s,password=%s,mobilenumber=%s,datetime=%s from users"
    # ,,DateTime=%s"
    mycur.execute(sql, [fullname, user_name, password, phoneNum, DateTime])
    results = mycur.fetchall()



def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x200+0+0")
    Label(fail, text="Login Unsuccessful..", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()
    if messagebox.askyesno("Do you want to retun to main Sceen?") ==True:
        main_screen()


def login_varify():
    """this info must be stored in a db for logged in users"""
    global user_name
    global password
    global fullname
    global phoneNum
    user_name = username_varify.get()
    password = password_varify.get()
    fullname=fullname_verify.get()
    phoneNum =cellphone_verify.get()

    db = pymysql.connect(host="localhost", user="root", passwd="", database="LifechoicesOnline")
    # global mycur
    mycur = db.cursor()
    DateTime = now.strftime("%Y-%m-%d %H:%M")
    sql = "select  fullname=%s, username=%s,password=%s,mobilenumber=%s,datetime=%s from users"
    #,,DateTime=%s"
    mycur.execute(sql,[fullname,user_name,password,phoneNum,DateTime])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged() #make a function that will insert the logged in username fullname andpassword ,
            #to table within
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Welcome to Lifechoices Online")
    root.geometry("600x600+0+0")
    root.configure(background="deep sky blue")
    Label(root,text="Welcome to Log-In Protal",font=("Arial",12,"bold"),bg="cadetblue",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="green2",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="green2",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Developed By Victor Nkuna",bg="deep sky blue").pack()

main_screen()
root.mainloop()
