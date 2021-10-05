from tkinter import *
import os
from PIL import ImageTk,Image
from  tkinter import  ttk
import mysql.connector
from tkinter import messagebox
import pygame
pygame.mixer.init()
import time
from itertools import count, cycle



flag=0
#button music
pygame.mixer.init()
def play():
    # pygame.mixer.music.load("C:\\Users\\NITRO5\\Downloads\\bsound.mp3")
    pygame.mixer.music.load("tkimg\\btn_click.mp3")
    pygame.mixer.music.play(loops=0)

#database
con= mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='aayush',
                    port=3306,
                    database='login')

print("successful")
cur=con.cursor()
#Main screen
root = Tk()
root.title('404 NOT FOUND')
root.geometry("1200x633")
root.resizable(0,0)
root.geometry("1200x633")
root.resizable(0,0)


canvas = Canvas(root, width=1200, height=633)
canvas.pack()

Background1= PhotoImage(file='tkimg\\rbg1.png')
B_image1 = canvas.create_image(0, 0, image=Background1, anchor=NW)

Back = PhotoImage(file='tkimg\\ff.png')
B_mage = canvas.create_image(599, 10, image=Back, anchor=NW)


def goto_homepage():
    root.destroy()
    os.system('python home.py')



def insert_value():
    # database


    # cur.execute("select * from record")
    # result = cur.fetchall()
    # for i in result:
    #     print(i)
    name=Name.get()
    last=Lname.get()
    user=username.get()
    emailid= Email.get()
    spassword= Password.get()
    cpassword= cpass.get()


    if name=='' or last==''or emailid=='' or spassword=='' or user=='' or cpassword=='':
        messagebox.showinfo("error","fill all details")
    elif spassword!=cpassword:
        messagebox.showinfo("error","password doesn't match")
    elif name.isalpha()!=True or last.isalpha()!=True:
        messagebox.showinfo("error", "enter only alphabets in first and last name")
    elif user.isalnum() != True:
        messagebox.showinfo("error", "enter alphaneumeric in username")
    else:
        cur = con.cursor()
        insert_stmt=(
            "INSERT INTO registration(fname,lname,username,emailid,password)"
            "VALUES (%s,%s,%s,%s,%s)"
            )


        data=(name,last,user,emailid,spassword)
        cur.execute(insert_stmt, data)
        con.commit()
        con.close()
        messagebox.showinfo("hurray","signup successfull")
        global flag
        flag=1
        goto_homepage()
    status=set_status(flag)


def get_status(flag_value):
    if flag_value==0:
        return "signup failed"
    else:
        return "signup successfull"




submit_img=Image.open("tkimg\\submit.png")
submit_img=ImageTk.PhotoImage(submit_img)

arrow_img = Image.open("tkimg\\arrow.png")
arrow_img = ImageTk.PhotoImage(arrow_img)

def set_status(flag):
    if flag==1:

       return "insert value completed"
    else:
        return "insert unsuccessful"

def signpage():
    global messaage;
    global Name
    global Lname
    global Email
    global Password
    global username
    global cpass

    Name=StringVar()
    Lname= StringVar()
    Email = StringVar()
    Password=StringVar()
    username=StringVar()
    cpass=StringVar()
    lname = Entry(root, bd=8, width=21, textvariable=Lname,relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                  fg='white')
    lname.place(x=350, y=217)

    username = Entry(root, bd=8, width=21,textvariable=username, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                     fg='white')
    username.place(x=350, y=290)

    Email = Entry(root, bd=8, width=21, textvariable=Email,relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                  fg='white')
    Email.place(x=350, y=360)




    fname = Entry(root, bd=8, width=21,textvariable=Name, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                  fg='turquoise3')
    fname.place(x=350, y=140)


    password = Entry(root, bd=8, width=21, textvariable=Password,relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                     fg='white')
    password.place(x=350, y=435)

    c_password = Entry(root, bd=8, width=21,textvariable=cpass, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                       fg='white')
    c_password.place(x=350, y=500)

    sub_btn = Button(root, image=submit_img, borderwidth=0, command=lambda: [play(),  insert_value()],
                     width=210, height=40, highlightthickness=3)
    sub_btn.place(x=745, y=570)

    back_btn = Button(root, image=arrow_img, width=150, borderwidth=0, height=50, relief=FLAT,
                      font=('arial', 14, 'bold'),
                      bg='#d33d10', fg='white', activebackground='#d33d10', command=lambda: [play(), goto_homepage()])
    back_btn.place(x=90, y=40)
    root.mainloop()

signpage()





