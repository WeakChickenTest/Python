from tkinter import *
from tkinter import messagebox

root = Tk()
btn01 = Button(root)
btn01["text"] = "点我就送花"

btn01.pack()

def songhua(e):
    messagebox.showinfo("Message","送你一朵玫瑰花，亲亲我吧")
    print("送你99朵玫瑰花")
btn01.bind("Button",songhua)

root.mainloop()