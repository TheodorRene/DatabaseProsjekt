import tkinter as tk
from tkinter import ttk
from tables import *

class main(tk.Tk):
    def __init(self,*args,**kwargs):
        tk.TK.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LandingPage, Treningsokt_page):
            frame = F(containger,self)
            self.frames[F] = frame
        self.show_frame(LandingPage)

    def show_frame(self, cont):
        fram = self.frames[cont]
        fram.tkraise()

class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(treningsokt_page))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",command=lambda: controller.show_frame(treningsokt_page))
        button2.pack()



class Treningsokt_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []
        self.num_values = [1,2,3,4,5,6,7,8,9,10]

        #trenings_id
        t_id = tk.Label(self, text="Treningsøkt id")
        t_id_ent = tk.Entry(self)
        widgets.extend([t_id,t_id_ent])
        ent.append(t_id_ent)

        #dato
        t_dato = tk.Label(self, text="Dato (YYYY-MM-DD")
        t_dato_ent = tk.Entry(self)
        widgets.extend([t_dato,t_dato_ent])
        ent.append(t_dato_ent)

        #varighet
        t_varighet = tk.Label(self, text="Varighet")
        t_varighet_ent = tk.Entry(self)
        widgets.extend([t_varighet,t_varighet_ent])
        ent.append(t_varighet_ent)

        #personlig form
        t_form = tk.Label(self, text="Personlig form")
        t_form_ent = ttk.Combobox(self,values = num_values)
        widgets.extend([t_form,t_form_ent])
        ent.append(t_form_ent)

        #personlig prestasjon
        t_prestasjon = tk.Label(self, text="Prestasjon")
        t_prestasjon_ent = ttk.Combobox(self,values = num_values)
        widgets.extend([t_prestasjon,t_prestasjon_ent])
        ent.append(t_prestasjon_ent)

        #senter_id
        t_senter_id = tk.Label(self, text="Senter id")
        t_senter_id_ent = tk.Entry(self)
        widgets.extend([t_senter_id,t_senter_id_ent])
        ent.append(t_senter_id_ent)

        #pnr
        t_pnr = tk.Label(self, text="Person nummer")
        t_pnr_ent = tk.Entry(self)
        widgets.extend([t_pnr,t_pnr_ent])
        ent.append(t_pnr_ent)

        #forteller tkinter at den skal legge på plass alle objektene våre
        for el in widgets:
            el.pack()
        #button
        but = tk.Button(self, text='Add to database', width=25, command=self.into_db)
        widgets.append(but)


    def into_db():
        #anbefaler å prøve å forstå linjen under, meget fornøyd med den hehe
        okt = Treningsokt(*[el.get() for el in ent])
        okt.save()


#viktig mainloop
app = main()
app.mainloop()



