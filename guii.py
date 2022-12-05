import tkinter
from tkinter import *
import random
import time
import asyncio
from threading import Event

# print("Human expression research #Day 01 by Sahil Thakur")
from self import self

root = Tk()
root.geometry("1200x700")
root.config(bg="white")
img = PhotoImage(file='a.png')
# for i in range (5):
#     a = Label(root, image=img, bg="white")
#     b = random.randint(0, 500)
#     c = random.randint(0, 700)
#     a.place(x=b, y=c)
#     time.sleep(2)
#     root.update_idletasks()
#     img = PhotoImage(file='c.png')

fc = PhotoImage(file='face.png')
face = Label(root, image=fc , bg="white")
face.place(x=550, y =70)

# a = Label(root, image=img, bg="#D9D9D9").place(x=933,y=220)


rteimg = PhotoImage(file='a.png')
rteye = Label(root, image=rteimg, bg="#D9D9D9")
rteye.place(x=902, y=220)

lteimg = PhotoImage(file='lye.png')
lteye = Label(root, image=lteimg, bg="#D9D9D9")
lteye.place(x=670, y=220)

for i in range(10):
    tym = random.randint(2, 10)

    rtex = random.randint(870,933)
    rtey = random.randint(185, 250)

    ltex = random.randint(635, 702)
    ltey = random.randint(185,250)



    rteimg = PhotoImage(file='a.png')
    rteye = Label(root, image=rteimg , bg = "black")
    rteye.place(x=rtex, y=rtey)
    root.update_idletasks()
    rteimg =PhotoImage(file='c.png')
    time.sleep(2)

    # letym = random.randint(2,10)


    ##########################################3
    lteimg = PhotoImage(file='lye.png')
    lteye = Label(root, image=lteimg, bg="black")
    lteye.place(x=ltex, y=ltey)
    root.update_idletasks()
    lteimg = PhotoImage(file='eee.png')
    # time.perf_counter()


    ##############################################


    # lteimg = PhotoImage(file='lye.png')
    # lteye = Label(root, image = lteimg, bg ="#D9D9D9")
    # lteye.place(x=ltex, y=ltey)
    # root.update_idletasks()
    # lteimg=PhotoImage(file='eee.png')
    # # root.update_idletasks()
    # time.sleep(2)




    # z = Label(root, text=tym).place(x= 100, y =100)






root.mainloop()