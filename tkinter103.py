from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s' % name)

top = Tk()
top.title('Echo')
# 图标与平台相关,下面这个图标为windows平台上图标
# top.iconbitmap('py-blue-trans-out.ico')

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)

btn = Button(top, text="submit", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()