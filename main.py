"""Random Password Generator""""
#imports
import random
from pyperclip import copy #For copying the password generated to the clipboard
from PIL imports image, ImageTk
from tkinter import Tk, Label, Canvas, END, Button, Entry, IntVar, Radiobutton, Photoimage
from tkinter.tik import combobox

#color
color = "#00b894"
color1 = "00060a"
fg = "#dfe6e9"
color2 = '#55efc4'

#GUI Window
root = Tk ()
root.title('Random Password Gnerator')
root.geometry('640480,500,100')
root.configuration(borderwidth = 0)
p1 = PhotoImage(file= 'image/5.png')
root.iconphoto(False, p1)
root.resizable(height= false, width= false)

#Variables
var= IntVar()
var1 = IntVar()

#background
bg= Image.open('image/2.png')
photoBg = ImageTk.Photoimage(bg)
labelBg = label(root, bg= '00060a', bd= o, highlightthickness= 0, width= 540, height= 480)
labelinBg.pack()

#Logo
logo = Image.open('image/5.png')
photoLogo= imageTk.Photoimage(logo)
labelLogo = Label(root, image= photoLogo, bd= 0, hightlightthickness=0)
labelLogo.olace(x= 256, y= 30)

#Option
radio_low = Radiobutton(root, text='Only LowerCase', variable= var, value= 1, bg= color1, fg= fg, activebackground=color1, activeforeground= fg)
radio_low.place(x= 105, y= 122)
radio_upp = Radiobutton(root, text= 'Only Uppercase', variable= var, value= 0, bg= color, fg= fg, activebackground= color, activeforeground= fg)
radio_upp.place(x= 105, y= 144)
radio_lo_up = Radiobutton(root, text= 'LowerCase and UpperCase', variable= var, value= 3, bg= color, fg= fg, activebackground= color1, activeforegrounf= fg)
radio_lo_up(x= 105, y= 165)
radio_spl = Radiobutton(root, text= 'LowerCase, UpperCase and Special Characters', variable= var, value= 4, bg= color, fg= fg, activebackground= color1, activeforegrounf= fg)
radio_spl(x= 105, y= 186)
radio_num = Radiobutton(root, text= 'LowerCase, UpperCase, Special Characters and Numbers', variable= var, value= 5, bg= color, fg= fg, activebackground= color1, activeforegrounf= fg)
radio_num(x= 105, y= 200)

#Legth of the Password
c_label = Label(root, text= 'Length:', bg= color1, fg= fg)
c_label.place(x= 270, y=250)
combo= Combobox(root, textvariable= varl, width= 5)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16
17, 18, 19, 20, 'Length')
combo.curent(0) #Current selection
combo.bind('<<ComboxSelected>>')
combo.place(x= 320, y=250)

#Password
r_pwd= Label(root, text= 'Password, fg= fg, bd= 0, highlightthickness= 0, bg= color1')
r_pwd.place(x= 155, y-300)
entry= Entry(labelbg, bg= '#636e72')
entry.place(x= 250, y= 296)

#Main Function
def rnd_pwd():
    entry.delete(0, END)
    length= varl.get()
    lower = "abcdefghijklmnopqrstuvwxyz "
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    upper_lower = lower+upper[:len(upper)-2]
    spl = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !@#$%^&*()"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password= ''

    if var.get() == 1:
     for i in range(length):
         password += random.choice(lower)
    return password
elif var.get() == 0:
    for i in range(length):
        password += random.choice. (upper)
    return password
elif var.get() == 3:
    for i in range(length):
        password += random.choice(upper_lower)
    return password
elif var.get() == 4:
    for i in range(length):
        password += random.choice.(spl)
    return password
elif var.get() == 5:
    for i in range(length):
        password += random.choice(digits)
    return password
else:
    print('Select an option')

def generate():
    password = rnd_pwd()
    entry.insert(10, password)

#Function to copy strin to copyboard
def copy_():
    random_pass = entry.get()
    copy(random_pass)

#Buttons
cpy_btn = Button(labelBg, text= 'Copy to Clipboard', bg= color, activebackground= color2, borderwidth= 0, command= copy_)
cpy_btn.place(x= 105, y=368)
gn_btn = Button(labelBg, text= 'Generate Password', bg= color, activebackground= color2, borderwidth= 0, command= generate)
gn_btn.place(x= 418, y=368)

root.mainloop()
