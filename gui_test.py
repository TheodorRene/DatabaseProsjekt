import tkinter as tk
from tkinter import ttk
from tables import *
from database import DB

#https://pythonprogramming.net/change-show-new-frame-tkinter/
class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LandingPage, Treningsokt_page, Last_N_TrainingExercisesPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(LandingPage)

    def show_frame(self, cont):
        fram = self.frames[cont]
        fram.tkraise()


class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Exersiceboi")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Ny treningsøkt", command=lambda: controller.show_frame(Treningsokt_page))
        button.pack()

        button2 = tk.Button(self, text="Treningsøkter",command=lambda: controller.show_frame(Last_N_TrainingExercisesPage))
        button2.pack()



class Treningsokt_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []
        self.num_values = [1,2,3,4,5,6,7,8,9,10]

        self.title = tk.Label(self, text="Legg til treningsøkt")
        self.widgets.append(self.title)

        #trenings_id
        t_id = tk.Label(self, text="Treningsøkt id")
        t_id_ent = tk.Entry(self)
        self.widgets.extend([t_id,t_id_ent])
        self.ent.append(t_id_ent)

        #dato
        t_dato = tk.Label(self, text="Dato (YYYY-MM-DD")
        t_dato_ent = tk.Entry(self)
        self.widgets.extend([t_dato,t_dato_ent])
        self.ent.append(t_dato_ent)

        #varighet
        t_varighet = tk.Label(self, text="Varighet")
        t_varighet_ent = tk.Entry(self)
        self.widgets.extend([t_varighet,t_varighet_ent])
        self.ent.append(t_varighet_ent)

        #personlig form
        t_form = tk.Label(self, text="Personlig form")
        t_form_ent = ttk.Combobox(self,values = self.num_values)
        self.widgets.extend([t_form,t_form_ent])
        self.ent.append(t_form_ent)

        #personlig prestasjon
        t_prestasjon = tk.Label(self, text="Prestasjon")
        t_prestasjon_ent = ttk.Combobox(self,values = self.num_values)
        self.widgets.extend([t_prestasjon,t_prestasjon_ent])
        self.ent.append(t_prestasjon_ent)

        #senter_id
        #Dette kan jo hentes fra databasen el[0] for el in con.execute(SELECT navn FROM treningsenter).fetchall();
        t_senter_id = tk.Label(self, text="Senter id")
        t_senter_id_ent = tk.Entry(self)
        self.widgets.extend([t_senter_id,t_senter_id_ent])
        self.ent.append(t_senter_id_ent)

        #pnr
        t_pnr = tk.Label(self, text="Personnummer")
        t_pnr_ent = tk.Entry(self)
        self.widgets.extend([t_pnr,t_pnr_ent])
        self.ent.append(t_pnr_ent)

        but = tk.Button(self, text='Legg til i database', width=25, command=self.into_db)
        self.widgets.append(but)

        #forteller tkinter at den skal legge på plass alle objektene våre
        for el in self.widgets:
            el.pack()
        #button

        home_button = tk.Button(self, text="Gå tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()


    def into_db(self):
        #anbefaler å prøve å forstå linjen under, meget fornøyd med den hehe
        okt = Treningsokt(*[el.get() for el in self.ent])
        okt.save()
        self.title.config(text="Databasen har blitt oppdatert")


class Last_N_TrainingExercisesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.num_values = [1,2,3,4,5,6,7,8,9,10]

        label = tk.Label(self, text="Dine siste øvelser")
        label.pack(pady=10,padx=10)

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10,padx=10)

        button = tk.Button(self, text="Hent fra database", command=self.getExercises)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

        self.num_ent = ttk.Combobox(self,values = self.num_values)
        self.num_ent.pack()

        self.pnr_ent = tk.Entry(self)
        self.pnr_ent.pack()

    def getExercises(self):
        el = DB.get_n_okter(int(self.num_ent.get()))
        string=""
        for liste in el:
            string += "----------------\n"
            string += f"Dato: {liste[0]}\nVarighet: {liste[1]}\nPersonlig form:{liste[2]}\nPrestasjon:{liste[3]}\nTreningssenter: {liste[4]}\n"
        self.results.config(text=string)



#viktig mainloop
app = main()
app.mainloop()



