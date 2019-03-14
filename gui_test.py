import tkinter as tk
from tkinter import ttk
from okt import treningsokt

root = tk.Tk()

w = tk.Label(root,text="Hello tkinter")

t = True

def showSomething():
    global t
    t = not t
    if t:
        w.config(text="you pressed button")
    else:
        w.config(text="you pressed nothing")

button = tk.Button(root, text='Show trening', width=25, command=showSomething)


widgets = []
ent = []
num_values = [1,2,3,4,5,6,7,8,9,10]

#trenings_id
t_id = tk.Label(root, text="Treningsøkt id")
t_id_ent = tk.Entry(root)
widgets.extend([t_id,t_id_ent])
ent.append(t_id_ent)

#dato
t_dato = tk.Label(root, text="Dato (YYYY-MM-DD")
t_dato_ent = tk.Entry(root)
widgets.extend([t_dato,t_dato_ent])
ent.append(t_dato_ent)

#varighet
t_varighet = tk.Label(root, text="Varighet")
t_varighet_ent = tk.Entry(root)
widgets.extend([t_varighet,t_varighet_ent])
ent.append(t_varighet_ent)

#personlig form
t_form = tk.Label(root, text="Personlig form")
t_form_ent = ttk.Combobox(root,values = num_values)
widgets.extend([t_form,t_form_ent])
ent.append(t_form_ent)

#personlig prestasjon
t_prestasjon = tk.Label(root, text="Prestasjon")
t_prestasjon_ent = ttk.Combobox(root,values = num_values)
widgets.extend([t_prestasjon,t_prestasjon_ent])
ent.append(t_prestasjon_ent)

#senter_id
t_senter_id = tk.Label(root, text="Senter id")
t_senter_id_ent = tk.Entry(root)
widgets.extend([t_senter_id,t_senter_id_ent])
ent.append(t_senter_id_ent)

#pnr
t_pnr = tk.Label(root, text="Person nummer")
t_pnr_ent = tk.Entry(root)
widgets.extend([t_pnr,t_pnr_ent])
ent.append(t_pnr_ent)


def into_db():
    #anbefaler å prøve å forstå linjen under, meget fornøyd
    okt = treningsokt(*[el.get() for el in ent])
    okt.save()


but = tk.Button(root, text='Add to database', width=25, command=into_db)
widgets.append(but)

#forteller tkinter at den skal legge på plass alle objektene våre
for el in widgets:
    el.pack()


root.mainloop()

