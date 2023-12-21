import tkinter as tk
from tkinter import ttk
from tkinter import font

# functions
def start():
    entry.focus()
    entry.config(font=font_custom)
    entry.pack(pady=30)
    button.pack_forget()
    button.pack(pady=30)
    button.config(text='Enter', command=lambda: idiom(list_idiom))
    win.unbind('<Return>')
    win.bind('<Return>', lambda event: idiom(list_idiom))
def idiom(l):
    if  var.get() == l[0]:
        var.set('')
        l.remove(l[0])
        if len(l) == 0:
            button.pack_forget()
            entry.pack_forget()
            ttk.Label(text = ' Game Over ',font=font_custom).pack(pady=25)
            win.unbind('<Return>')
            win.bind('<Return>', lambda event: win.destroy())
        else:
            entry.pack_forget()
            confirm = ttk.Label(text="correct",font=font_custom)
            confirm.pack(pady=25)
            button.config(text='next', command=lambda: (confirm.pack_forget() ,button.pack_forget(), entry.pack(pady=30),button.pack(pady=30) , button.config(text='Enter', command=lambda: idiom(list_idiom))))
            entry.focus()
    # here I want to modify the bind of win, How can I do that ?
            win.unbind('<Return>')
            win.bind('<Return>', lambda event: (confirm.pack_forget() ,button.pack_forget(), entry.pack(pady=30),button.pack(pady=30) , button.config(text='Enter', command=lambda: idiom(list_idiom)),win.unbind('<Return>'), win.bind     ('<Return>', lambda event : idiom(list_idiom))))
    else :
       var.set('')
       entry.focus()
    print(l)


# setup 
win = tk.Tk()
win.title('Idiom Podium')
win.geometry('720x480')

# font and style
font_custom = font.Font(size = 24)
style = ttk.Style()
style.configure('TButton',font = 24)


# list idiom
list_idiom = ['Break the ice','Get off on the wrong foot','Get on like a house on fire','Get on someone\'s nerves','Give someone the cold shoulder','Go back a long way (british)/Go way back','Hit it off','Sparks fly','Your own flesh and blood','Leave someone in the lurch','On the rocks','On the same wavelength','Save face']

label = ttk.Label(win, text = 'Relationships',font=font_custom)
label.pack(pady=50)

var = tk.StringVar()


entry = ttk.Entry(win, textvariable=var)


button = ttk.Button(win, text= 'Start', command= start)
button.pack(pady=10)

win.bind('<Return>', lambda event : start())
# run
win.mainloop()