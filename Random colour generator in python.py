from tkinter import *
import random as rdn
from colour import Color

root = Tk()

root.geometry('500x500')
root.title("P-155")
root.configure(bg='snow')

color = {"r":255,
         "g":255,
         "b":255}

def random_color_val():
    global random_r
    random_r = color["r"]
    global random_r_num
    random_r_num = rdn.randint(0, random_r)
    
    global random_g
    random_g = color["g"]
    global random_g_num
    random_g_num = rdn.randint(0, random_g)
    
    global random_b
    random_b = color["b"]
    global random_b_num
    random_b_num = rdn.randint(0, random_b)
    change()

def change():
    color = '#%02x%02x%02x' % (random_r_num, random_g_num, random_b_num)
    print(color)
    print(random_r_num, random_g_num, random_b_num)
    root['bg']=color
    btn['bg']=color
    c = Color(color)
    btn['text']=c
    
btn = Button(root, fg='black', text="Change", command=random_color_val)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
