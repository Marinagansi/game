from tkinter import *
import os
from PIL import ImageTk,Image
from  tkinter import  ttk
import mysql.connector
from tkinter import messagebox
import pygame
#button music
pygame.mixer.init()
def play():
    # pygame.mixer.music.load("C:\\Users\\NITRO5\\Downloads\\bsound.mp3")
    pygame.mixer.music.load("bsound.mp3")
    pygame.mixer.music.play(loops=0)

#database
con= mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='Gansi@974111',
                    port=3306,
                    database='login')
print("successful")
cur=con.cursor()
#Main screen
root = Tk()
root.title('Movie Ticketing System')
root.geometry("637x688")
root.resizable(0,0)
root.geometry("638x689")
root.resizable(0,0)
pic=Image.open('CREATE ACC.png')
ren=ImageTk.PhotoImage(pic)
img=Label(root,image=ren)
img.place(x=0,y=0)

def goto_homepage():
    root.destroy()
    os.system('python home.py')


def insert_value():
    # database

    # cur = con.cursor()
    # cur.execute("select * from record")
    # result = cur.fetchall()
    # for i in result:
    #     print(i)


    name=Name.get()
    last=Lname.get()
    emailid=Email.get()
    spassword=Password.get()
    phone1=Phone.get()
    cpassword=cpass.get()

    if name=='' or last==''or emailid=='' or spassword=='' or phone1=='' or cpassword=='':
        messagebox.showinfo("fill the empty fiels!!")
        #  if spassword==cpassword:
        # #     messagebox.showinfo("password doesn't match")



    cur=con.cursor()

    insert_stmt=(
         "INSERT INTO registration(fname,lname,emailid,phone,password,c_password)"
         "VALUES (%s,%s,%s,%s,%s,%s)"
     )
    data = (name, last, emailid, spassword, phone1,cpassword)
    cur.execute(insert_stmt, data)
    con.commit()



submit_img=Image.open("submit.png")
submit_img=ImageTk.PhotoImage(submit_img)




def signpage():
    global messaage;
    global Name
    global Lname
    global Email
    global Password
    global Phone
    global cpass

    Name=StringVar()
    Lname= StringVar()
    Email = StringVar()
    Password=StringVar()
    Phone=StringVar()
    cpass=StringVar()


    fname = Entry(root, bd=8, width=21,textvariable=Name, relief=FLAT, font=('arial', 14, 'bold'), bg='#385273', fg='turquoise3')
    fname.place(x=260, y=210)

    lname = Entry(root, bd=8, width=21, textvariable=Lname,relief=FLAT, font=('arial', 14, 'bold'), bg='#385273', fg='white')
    lname.place(x=260, y=260)

    email = Entry(root, bd=8, width=21,textvariable=Email, relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='white')
    email.place(x=260, y=310)

    phone = Entry(root, bd=8, width=21, textvariable=Phone,relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='white')
    phone.place(x=260, y=360)

    password = Entry(root, bd=8, width=21, textvariable=Password,relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='white')
    password.place(x=260, y=407)

    c_password = Entry(root, bd=8, width=21,textvariable=cpass, relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='white')
    c_password.place(x=260, y=458)

    sub_btn = Button(root, image=submit_img, borderwidth=0, command=lambda: [play(),  insert_value(),goto_homepage()],
                     width=287, height=53, highlightthickness=3)
    sub_btn.place(x=200, y=510)


    root.mainloop()

signpage()

#
# if name.get()!="" and user.get()!="" and password.get()!="" and confirm.get()!="" and email.get()!="":
#     if password.get()==confirm.get():
#         c.execute("""INSERT INTO user_info VALUES(:full_name,:user_name,:password,:email,:type
#         )""",{
#             'full_name':name.get(),
#             'user_name':user.get(),
#             'password':password.get(),
#             'email':email.get(),
#             'type':position
#             })
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("attention", "detail submitted")
#     else:
#         messagebox.showinfo("error!","password doesn't match")
# else:
#         messagebox.showinfo("please", "fill all detail")



