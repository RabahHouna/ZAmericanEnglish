# 07 Involvement and interest
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


win = tk.Tk()
win.title('Idiom Podium')
win.geometry('720x480')

# font and style
font_custom = font.Font(size = 24)
style = ttk.Style()
style.configure('TButton',font = 24)


# list idiom
list_idiom = ['(Not) your cup of tea','Have an ax to grind','In the picture','Jump on the bandwagon','Keep a low profile','A labor of love','Mean business','A nosey parker','Poke/Stick your nose into something (informal)','Keep your nose out of something (informal)','Steer clear of something','Try your hand at something','Up to your ears','Whet someone\'s appetite','Your heart isn\'t in something']

label = ttk.Label(win, text = 'Involvement and interest',font=font_custom)
label.pack(pady=50)

var = tk.StringVar()


entry = ttk.Entry(win, textvariable=var)


button = ttk.Button(win, text= 'Start', command= start)
button.pack(pady=10)

win.bind('<Return>', lambda event : start())
# run
win.mainloop()