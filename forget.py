from tkinter import *
import os
from PIL import ImageTk,Image
from  tkinter import  ttk
import mysql.connector
from tkinter import messagebox
import pygame
pygame.mixer.init()
def play():
    # pygame.mixer.music.load("C:\\Users\\NITRO5\\Downloads\\bsound.mp3")
    pygame.mixer.music.load("tkimg\\btn_click.mp3")
    pygame.mixer.music.play(loops=0)

def goto_loginpage():
    root.destroy()
    os.system('python login.py')

# Main screen
root = Tk()
root.title('404 NOT FOUND')
root.geometry("1200x633")
root.resizable(0, 0)
root.geometry("1200x633")
root.resizable(0, 0)


canvas = Canvas(root, width=1200, height=633)
canvas.pack()
Background1= PhotoImage(file='tkimg\\resetbg.png')
B_image1 = canvas.create_image(0, 0, image=Background1, anchor=NW)
#database
con= mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='Gansi@974111',
                    port=3306,
                    database='login')

print("successful")
cur=con.cursor()


def update():
    name = Name.get()
    last = Lname.get()
    user = username.get()
    emailid = Email.get()
    spassword = Password.get()
    cpassword = cpass.get()
    cur = con.cursor()
    # try:lname=?,username=?,emailid=?
    if user == '' :
        messagebox.showinfo("error", "fill all details")
        return;
    elif spassword != cpassword:
        messagebox.showinfo("error", "password doesn't match")
        return;
    else:
        insert_stmt = (
                """update  registration set password=%s  where username=%s""")
        value=( Password.get(),username.get())

        #execute the sql commad

        cur.execute(insert_stmt,value)
        con.commit()
        con.close()
        messagebox.showinfo("hurray", "update successfull")

        goto_loginpage()
    # except:
    #     con.rollback()
    #rollback in case there is any error



def change():
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



    username = Entry(root, bd=8, width=21, textvariable=username, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273',
                     fg='white')
    username.place(x=570, y=440)

    password = Entry(root, bd=8, width=21, textvariable=Password,relief=FLAT, font=('arial', 14, 'bold'), bg='#385273', fg='white')
    password.place(x=570, y=497)

    c_password = Entry(root, bd=8, width=21,textvariable=cpass, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273', fg='white')
    c_password.place(x=570, y=555)

    sub_btn = Button(root, text="update",relief=FLAT,font=('arial', 14, 'bold'), bg='#405669',fg='white',  command=lambda: [play(),  update()],
                     width=14, height=1, highlightthickness=3)
    sub_btn.place(x=839, y=548)

    mainloop()
change()