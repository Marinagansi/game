from tkinter import *
import os
from PIL import ImageTk,Image
import mysql.connector
import pygame
#button music
pygame.mixer.init()
def play():
    pygame.mixer.music.load("C:\\Users\\NITRO5\\Downloads\\bsound.mp3")
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
root.title('Movie Ticketing System')
root.geometry("637x688")
root.resizable(0,0)
root.geometry("637x688")
root.resizable(0,0)
pic=Image.open('Login.png')
renr=ImageTk.PhotoImage(pic)
img=Label(root,image=renr)
img.place(x=0,y=0)

def goto_homepage():
    root.destroy()
    os.system('python home.py')




load=Image.open("id icon.png")
render=ImageTk.PhotoImage(load)
img1=Label(root,image=render,bd=4)
img1.place(x=165,y=292)

load=Image.open("password icon.png")
ren=ImageTk.PhotoImage(load)
img2=Label(root,image=ren,bd=4)
img2.place(x=165,y=370)

login_img=Image.open("loginbtn.png")
login_img=ImageTk.PhotoImage(login_img)



std_id=Entry(root,bd=13,width=21,relief=FLAT, font=('arial',14,'bold'), bg='#00437c', fg='turquoise3',highlightthickness=3)
std_id.config(highlightbackground="white",highlightcolor="white")
std_id.place(x=220,y=370)

last=Entry(root,bd=13,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white',highlightthickness=3)
std_id.config(highlightbackground="white",highlightcolor="white")
last.place(x=220,y=292)



login_btn=Button(root,image=login_img,width=287,height=53,borderwidth=0,font=("arial",14,'bold'),command=lambda:[play(),goto_homepage()])
login_btn.place(x=200,y=510)

root.mainloop()