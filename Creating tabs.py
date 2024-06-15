from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.pack(expand=True,fill="both")
#fill = fill space on x and y axis

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack()
Label(tab1,text="Hello this is tab number 1",width=50,height=25).pack()
Label(tab2,text="Hello this is tab number 2",width=50,height=25).pack()


window.mainloop()
