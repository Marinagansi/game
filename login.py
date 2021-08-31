from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import pygame
from itertools import count, cycle
pygame.mixer.init()
import time;

class ImageLabel(Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


pygame.mixer.music.load("tkimg\\rbs.mp3")
pygame.mixer.music.play(loops=3)
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


def play():
    pygame.mixer.music.load("tkimg\\bsound.mp3")
    pygame.mixer.music.play(loops=0)


##dtabase
con= mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='20july4V',
                    port=3306,
                    database='login')
print("successful")
cur=con.cursor()


#Main screen
root = Tk()
root.title('404 NOT FOUND')
# root.geometry("637x688")
root.resizable(0,0)
root.geometry("1200x633")
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
    os.system('python part7.py')


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
        messagebox.showinfo("error","invalid user name and password")

def login():
    # animation
    xvelocity = 1
    yvelocity = 2



    global username
    global userpass
    username=StringVar()
    userpass=StringVar()

    canvas = Canvas(root, width=1200, height=633)
    canvas.pack()

    Background = PhotoImage(file='tkimg\\bbbgg.png')
    B_image = canvas.create_image(0, 0, image=Background, anchor=NW)

    lbl = ImageLabel(root)
    lbl.place(x=200, y=68, height=500, width=255)
    lbl.load('tkimg\\Robot.gif')
    # lbl.load('D:\\LKG\\robot11.gif')
    pygame.mixer.init()

    # load = Image.open("tkimg\\id icon.png")
    # render = ImageTk.PhotoImage(load)
    # img1 = Label(root, image=render, bd=4)
    # img1.place(x=165, y=292)
    #
    # load = Image.open("tkimg\\password icon.png")
    # ren = ImageTk.PhotoImage(load)
    # img2 = Label(root, image=ren, bd=4)
    # img2.place(x=165, y=370)

    login_img = Image.open("tkimg\\loginbtn.png")
    login_img = ImageTk.PhotoImage(login_img)

    username = Entry(root, bd=13, width=19,textvariable=username, relief=FLAT, font=('arial', 14, 'bold'), bg='#820609',
                   highlightthickness=3)
    username.config(highlightbackground="white", highlightcolor="white")
    username.place(x=790, y=110)#292

    last = Entry(root, bd=13, width=19,textvariable=userpass, relief=FLAT, font=('arial', 14, 'bold'), bg='#820609',
                 highlightthickness=3)
    last.config(highlightbackground="white", highlightcolor="white")
    last.place(x=790, y=210)

    login_btn = Button(root, image=login_img, width=100, height=50, borderwidth=0, font=("arial", 14, 'bold'),bg="#220515",
                       command=lambda: [play(),login_verfication()])
    login_btn.place(x=1090, y=170)

    # photo = PhotoImage(file='C:\\Users\\NITRO5\\Downloads\\robu.png')
    # image = canvas.create_image(0, 300, image=photo, anchor=NW)

    # image_width = photo.width()
    # image_height = photo.height()

    # while True:
    #     coordinates = canvas.coords(image)
    #
    #     # print(coordinates)
    #     if (coordinates[0] >= (500 - image_width) or (coordinates[0] < 0)):
    #         xvelocity = -xvelocity
    #     if (coordinates[1] >= (660 - image_height) or (coordinates[1] < 0)):
    #         yvelocity = -yvelocity
    #     canvas.move(image, xvelocity,yvelocity)
    #     root.update()
    #     time.sleep(0.01)

    root.mainloop()

login()
