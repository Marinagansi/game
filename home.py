from tkinter import *
import os
from PIL import ImageTk,Image
import pygame
pygame.mixer.init()
import time
from itertools import count, cycle

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



def play():
    pygame.mixer.music.load("tkimg\\btn_click.mp3")
    pygame.mixer.music.play(loops=0)

#assign velocity
xvelocity=1
yvelocity=2
Xvelocity=2
Yvelocity=1
xvelocity1=2
yvelocity1=2

#Main screen
master = Tk()
master.title('404 NOT FOUND')

master.geometry("1200x633")
master.resizable(0,0)

#canvas
canvas=Canvas(master,width=1200,height=633)
canvas.pack()

#
Background = PhotoImage(file='tkimg\\snwbg.png')
B_image=canvas.create_image(0,0,image=Background,anchor=NW)









lbl = ImageLabel(master)
lbl.place(x=830, y=405, height=180, width=365)
lbl.load('C:\\Users\\NITRO5\\Downloads\\wlc-unscreen (4).gif')
# lbl.load('tkimg\\snow.gif')

photo_image = PhotoImage(file='tkimg\\Ellipse 1.png')
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)

image2 = PhotoImage(file='tkimg\\blue eclips.png')
mimage2=canvas.create_image(50,0,image=image2,anchor=NW)

image3 = PhotoImage(file='tkimg\\blue eclips.png')
mimage3=canvas.create_image(180,0,image=image2,anchor=NW)



#image width and height
image_width=photo_image.width()
image_height=photo_image.height()

image_width1=image2.width()
image_height1=image2.height()
def goto_sign():
    master.destroy()
    os.system('python signuppage.py')

def goto_login():
    master.destroy()
    os.system('python login.py')






#button
std_login_btn=Button(master,text="sign in",width=8,height=1,relief= FLAT, font=('Comic Sans MS',30,'bold italic'), bg='#9AAACB', fg='white',activebackground='#9AAACB' , command =lambda:[play(),goto_login()])

std_login_btn.place(x=880,y=40)


login_btn=Button(master,text="Create Account",width=13,height=1,relief= FLAT,border=0, font=('Comic Sans MS',25,'bold italic'), bg='#9AAACB', fg='white',activebackground='#9AAACB',command= lambda:[play(),goto_sign()])
login_btn.place(x=855,y=135)


#animation
while True:
    coordinates=canvas.coords(my_image)

   #print(coordinates)
    if(coordinates[0]>=(500-image_width) or (coordinates[0]<0)):
        xvelocity= -xvelocity
    if (coordinates[1] >= (600- image_height) or (coordinates[1] < 0)):
        yvelocity = -yvelocity
    if (coordinates[0] >= (360 - image_width1) or (coordinates[0] < 0)):
        Xvelocity = -Xvelocity
    if (coordinates[1] >= (700 - image_height1) or (coordinates[1] < 0)):
        Yvelocity = -Yvelocity
    if (coordinates[0] >= (380 - image_width1) or (coordinates[0] < 0)):
        xvelocity1 = -xvelocity1
    if (coordinates[1] >= (600 - image_height1) or (coordinates[1] < 0)):
        yvelocity1 = -yvelocity1
    canvas.move(my_image, xvelocity, yvelocity)
    canvas.move(mimage2, Xvelocity, Yvelocity)

    canvas.move(mimage3, xvelocity1, yvelocity1)
    master.update()
    time.sleep(0.01)


master.mainloop()