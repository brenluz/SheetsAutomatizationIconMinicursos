from tkinter import ttk
from tkinter import *

def checkUrl(*args):
    try:
        value = url.get()
    except ValueError:
        pass


# Create the root window
root = Tk()
root.title('Sheet Automator')

# Create the main container
mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

# Cria uma entrada para o usuario colocar a url da planilha
url = StringVar()
entry = ttk.Entry(mainFrame, width=7 , textvariable=url)
entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Cria um botao para o usuario clicar e verificar a url
ttk.Button(mainFrame, text="Enter the Url", command=checkUrl).grid(column=3, row=3, sticky=W) 

ttk.Label(mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="meters").grid(column=3, row=2, sticky=W)

for child in mainFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5) # Add padding to all widgets
entry.focus() # Focus on the entry widget
root.bind("<Return>", checkUrl) # bind(key, function) binds a key press to a function

root.mainloop() 