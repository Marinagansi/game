from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import pygame
pygame.mixer.init()
import time;


#button music
def show_found_status(name,pw):
    cur = con.cursor()
    cur.execute("Select * from registration WHERE username=%s and password=%s",
              (name, pw))
    found = cur.fetchone()
    if found:
        return "account found"
    else:
        return "account not found"

pygame.mixer.init()
def play():
    pygame.mixer.music.load("tkimg\\bsound.mp3")
    pygame.mixer.music.play(loops=0)


##dtabase
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
root.title('404 NOT FOUND')
# root.geometry("637x688")
root.resizable(0,0)
root.geometry("637x688")
root.resizable(0,0)
# pic=Image.open('Login.png')
# renr=ImageTk.PhotoImage(pic)
# img=Label(root,image=renr)
# img.place(x=0,y=0)

def goto_homepage():
    root.destroy()
    os.system('python home.py')

def goto_game():
    root.destroy()
    os.system('python game_four.py')


def login_verfication():
    name = username.get()
    password = userpass.get()
    sql="select * from registration where username=%s and password=%s"
    cur.execute(sql,[(name),(password)])
    result=cur.fetchall()

    if result:
        for i in result:

            goto_game()
            break
    else:
        messagebox.showinfo("error","ivalid user name and password")

def login():
    # animation
    xvelocity = 1
    yvelocity = 2



    global username
    global userpass
    username=StringVar()
    userpass=StringVar()

    canvas = Canvas(root, width=637, height=688)
    canvas.pack()

    Background = PhotoImage(file='tkimg\\Login.png')
    B_image = canvas.create_image(0, 0, image=Background, anchor=NW)


    load = Image.open("tkimg\\id icon.png")
    render = ImageTk.PhotoImage(load)
    img1 = Label(root, image=render, bd=4)
    img1.place(x=165, y=292)

    load = Image.open("tkimg\\password icon.png")
    ren = ImageTk.PhotoImage(load)
    img2 = Label(root, image=ren, bd=4)
    img2.place(x=165, y=370)

    login_img = Image.open("tkimg\\loginbtn.png")
    login_img = ImageTk.PhotoImage(login_img)

    username = Entry(root, bd=13, width=21,textvariable=username, relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='turquoise3',
                   highlightthickness=3)
    username.config(highlightbackground="white", highlightcolor="white")
    username.place(x=220, y=292)#292

    last = Entry(root, bd=13, width=21,textvariable=userpass, relief=FLAT, font=('arial', 14, 'bold'), bg='#00437c', fg='white',
                 highlightthickness=3)
    last.config(highlightbackground="white", highlightcolor="white")
    last.place(x=220, y=370)

    login_btn = Button(root, image=login_img, width=210, height=50, borderwidth=0, font=("arial", 14, 'bold'),
                       command=lambda: [play(),login_verfication()])
    login_btn.place(x=215, y=490)

    photo = PhotoImage(file='tkimg\\chargame.png')
    image = canvas.create_image(0, 0, image=photo, anchor=NW)

    image_width = photo.width()
    image_height = photo.height()

    while True:
        coordinates = canvas.coords(image)

        # print(coordinates)
        if (coordinates[0] >= (290 - image_width) or (coordinates[0] < 0)):
            xvelocity = -xvelocity
        if (coordinates[1] >= (700 - image_height) or (coordinates[1] < 0)):
            yvelocity = -yvelocity
        canvas.move(image, xvelocity, 0)
        root.update()
        time.sleep(0.01)

    root.mainloop()

login()
