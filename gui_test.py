import tkinter as tk

root = tk.Tk()

w = tk.Label(root,text="Hello tkinter")

def showSomething():
    w.config(text="you pressed button")

w.pack()
button = tk.Button(root, text='Show trening', width=25, command=showSomething())
n = tk.Button(root, text='Stop', width=25, command=root.destroy)

button.pack()
n.pack()

root.mainloop()

