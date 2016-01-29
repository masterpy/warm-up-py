from tkinter import *
import random



fontsize = 30

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']

def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFlip)

def onGrow():
    global fontsize
    fontsize += 5

    mainLabel.config(font=('Consolas', fontsize, 'italic')

# after：将本组件于所选组建对象之后pack，类似于先创建选定组件再创建本组件
    main.after(100, onGrow)

main = Tk()
mainLabel = Label(main, text="Fun Gui", relief=RAISED)
mainLabel.config(font=('Consolas', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', command=onSpam).pack(fill=X)
Button(main, text='flip', command=onFlip).pack(fill=X)
Button(main, text='grow', command=onGrow).pack(fill=X))
main.mainloop()