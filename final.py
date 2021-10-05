from tkinter import *
import os
from PIL import ImageTk,Image
import pygame
pygame.mixer.init()
import time
from itertools import count, cycle

root = Tk()
root.title('404 NOT FOUND')
root.geometry("1200x633")
root.resizable(0,0)
root.geometry("1200x633")
root.resizable(0,0)

xvelocity=1
yvelocity=2
Xvelocity=2
Yvelocity=1
xvelocity1=2
yvelocity1=2

canvas = Canvas(root, width=1200, height=633)
canvas.pack()

Background1= PhotoImage(file='tkimg\\final info.png')
B_image1 = canvas.create_image(0, 0, image=Background1, anchor=NW)

photo_image = PhotoImage(file='tkimg\\star blue.png')
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)

image2 = PhotoImage(file='tkimg\\star red.png')
mimage2=canvas.create_image(50,0,image=image2,anchor=NW)

image_width=photo_image.width()
image_height=photo_image.height()


image_width1=image2.width()
image_height1=image2.height()

#animation
while True:
    coordinates=canvas.coords(my_image)

   #print(coordinates)
    if(coordinates[0]>=(700-image_width) or (coordinates[0]<0)):
        xvelocity= -xvelocity
    if (coordinates[1] >= (600- image_height) or (coordinates[1] < 0)):
        yvelocity = -yvelocity
        if (coordinates[0] >= (350 - image_width1) or (coordinates[0] < 0)):
            Xvelocity = -Xvelocity
        if (coordinates[1] >= (700 - image_height1) or (coordinates[1] < 0)):
            Yvelocity = -Yvelocity


        yvelocity1 = -yvelocity1
    canvas.move(my_image, xvelocity, yvelocity)
    canvas.move(mimage2, Xvelocity, Yvelocity)

    root.update()
    time.sleep(0.01)


root.mainloop()