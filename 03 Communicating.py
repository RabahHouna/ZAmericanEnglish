import tkinter as tk
from tkinter import ttk
from tkinter import font

# functions 
def idiom(l):
    
    if  var.get() == l[0]:
        var.set('')
        l.remove(l[0])
        if len(l) == 0:
            button.pack_forget()
            entry.pack_forget()
            ttk.Label(text = ' Game Over ', font=font_cust).pack(padx=10)
            win.unbind('<Return>')
            win.bind('<Return>', lambda event: win.destroy())
        else:
            entry.pack_forget()
            confirm = ttk.Label(text="correct", font=font_cust)
            confirm.pack(pady=25)
            button.config(text='next', command=lambda: (confirm.pack_forget() ,button.pack_forget(), entry.pack(pady=30),button.pack(pady=10) , button.config(text='Enter', command=lambda: idiom(list_idiom))))
    # here I want to modify the bind of win, How can I do that ?
            win.unbind('<Return>')
            win.bind('<Return>', lambda event: (confirm.pack_forget() ,button.pack_forget(), entry.pack(pady=30),button.pack(pady=10) , button.config(text='Enter', command=lambda: idiom(list_idiom)),win.unbind('<Return>'), win.bind     ('<Return>', lambda event : idiom(list_idiom))))
    else :
       var.set('')
    print(l)


# setup 
win = tk.Tk()
win.title('Idiom Podium')
win.geometry('720x480')

# style and font
font_cust = font.Font(size=24)
style = ttk.Style()
style.configure('TButton', font=24)

list_idiom = ['At cross purposes','Come out of your shell','Bring you out of your shell','Find common ground','From the horse\'s mouth','Get your wires/lines crossed','Go off on/at a tangent','Hear something through/on the grapevine','In black and white','In the loop','Keep someone posted','Let the cat out of the bag','Put someone in the picture','Spill the beans','Touch base']

label = ttk.Label(win, text = 'Communicating',font=font_cust)
label.pack(pady=50)

var = tk.StringVar()


entry = ttk.Entry(win, textvariable=var, font=font_cust)
entry.pack(pady = 30)
entry.focus()

button = ttk.Button(win, text= 'Enter', command=lambda : idiom (list_idiom))
button.pack(pady=10)

win.bind('<Return>', lambda event : idiom(list_idiom))
# run
win.mainloop()