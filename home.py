from tkinter import *
import pygame
import os
from PIL import ImageTk,Image
import pygame
pygame.mixer.init()
def play():
    pygame.mixer.music.load("bsound.mp3")
    pygame.mixer.music.play(loops=0)
#Main screen
master = Tk()
master.title('404 NOT FOUND')

master.geometry("639x698")
master.resizable(0,0)
load=Image.open("Login.png")
render=ImageTk.PhotoImage(load)
img=Label(master,image=render)
img.place(x=0,y=0)




def goto_sign():
    master.destroy()
    os.system('python signuppage.py')

def goto_login():
    master.destroy()
    os.system('python login.py')



sn_img=Image.open("snbutton.png")
sn_img=ImageTk.PhotoImage(sn_img)

ca_img=Image.open("ca button.png")
ca_img=ImageTk.PhotoImage(ca_img)




#button
std_login_btn=Button(master,image=sn_img,width=255,height=40,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c',  command =lambda:[play(),goto_login()])
std_login_btn.place(x=187,y=300)


login_btn=Button(master,image=ca_img,width=255,height=40,relief= FLAT,border=0, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c',command= lambda:[play(),goto_sign()])
login_btn.place(x=187,y=390)

master.mainloop()