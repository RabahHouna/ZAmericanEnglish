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
list_idiom = ['Get the hang of something','Get the picture','Get (hold of) the wrong end of the stick (informal)','Get your head around something','Go in one ear and out the other','A gray area','Not have a clue (informal)' ,'Put two and two together','Put two and two together and make five','Read between the lines','Jump to conclusions','Up to speed','Take something on board (british)']

label = ttk.Label(win, text = 'Knowledge and understanding',font=font_custom)
label.pack(pady=50)

var = tk.StringVar()


entry = ttk.Entry(win, textvariable=var)


button = ttk.Button(win, text= 'Start', command= start)
button.pack(pady=10)

win.bind('<Return>', lambda event : start())
# run
win.mainloop()