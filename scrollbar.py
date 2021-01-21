from tkinter import *
screen = Tk()
screen.geometry('400x400')
scrollbar_tk = Scrollbar(screen)
scrollbar_tk.pack(side=RIGHT, fill=Y)
listbox_tk = Listbox(screen, yscrollcommand=scrollbar_tk.set)
for i in range(100):
    listbox_tk.insert(END, str(i))
listbox_tk.pack(side=LEFT, fill=BOTH)
scrollbar_tk.config(command=listbox_tk.yview)
mainloop()