import random
import time
from tkinter import *


root = Tk()
root.geometry("1200x700")

# w = 600
# h = 400
# x = w/2
# y = h/2

mc = Canvas(root, width=1200 , height=700, bg = "white")
mc.pack(pady=20)



img = PhotoImage(file='ssign.png')

for i in range(3):
    p = random.randint(0,500)
    s = random.randint(0,500)
    mimg = mc.create_image(0,0, anchor=NW , image= img)
    mc.move(mimg, s, p)









root.mainloop()