#! /usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tables import *
from database import DB
from functions import GuiTools as gt

#https://pythonprogramming.net/change-show-new-frame-tkinter/

class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        pages = [LandingPage, Treningsokt_page, Last_N_TrainingExercisesPage, ApparatPage, OvelsePage, RegisterOvelsegruppePage, AddOvelseToOvelsegruppePage, RetrieveOvelseInOvelsegruppePage, IntervallLoggPage,PersonalRecordPage,AddOvelseTreningsoktPage]
        for F in pages:
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(LandingPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
















class RetrieveOvelseInOvelsegruppePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.widgets = []

        #self.ovelsegrupper=["Ben","Armer", "Hode"]
        self.ovelsegrupper = [el[0] for el in DB.get_ovelsegrupper()]
        ovelsegruppe_navn=DB.get_ovelsegrupper

        #for row in ovelsegruppe_navn:                      #Vil ikke iterere over en fetchall, hvordan får jeg liste med navn da?
           # self.ovelsegrupper.append(row[0])

        self.title = tk.Label(self, text="Velg ovelsegruppe")
        self.widgets.append(self.title)

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10, padx=10)


        """gruppe_id = tk.Label(self, text="Ovelsegruppe id")
        self.gruppe_id_ent = tk.Entry(self)
        self.widgets.extend([gruppe_id, self.gruppe_id_ent])"""

        self.name_ent = ttk.Combobox(self, values=self.ovelsegrupper)
        self.name_ent.pack()



        button = tk.Button(self, text="Hent fra database", command=self.get_ovelser)

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)
    #def get_id_ovelsegruppe(self):
        #el=DB.get_id_of_ovelsegruppe(self.name_ent.get())
        #return el #Kan man returnere noe her?

    def get_ovelser(self):
        ovelsegruppe_id=DB.get_id_of_ovelsegruppe(self.name_ent.get())
        print(ovelsegruppe_id)
        ovelsegrupper=DB.get_ovelser_in_ovelsegruppe(ovelsegruppe_id)
        print(ovelsegrupper)
         #Må endre sånn at man skaffer riktig info
        string = "Ovelser:\n"
        for liste in ovelsegrupper:
            string += f"{liste}\n"
        self.results.config(text=string)


class IntervallLoggPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []
        self.all_ovelse = DB.project_table('ovelse', 'navn')

        self.title = tk.Label(self, text="Se intervallogg")
        self.widgets.append(self.title)

        t_id = tk.Label(self, text="Øvelse")
        self.t_form_comb = ttk.Combobox(self, values=self.all_ovelse)
        self.widgets.extend([t_id,self.t_form_comb])
        self.ent.append(self.t_form_comb)

        #dato start
        self.t_dato_start = tk.Label(self, text="Intervall start: (YYYY-MM-DD")
        self.t_dato_start_ent = tk.Entry(self)
        self.widgets.extend([self.t_dato_start,self.t_dato_start_ent])
        self.ent.append(self.t_dato_start_ent)

        # dato end
        self.t_dato_end = tk.Label(self, text="Intervall slutt: (YYYY-MM-DD")
        self.t_dato_end_ent = tk.Entry(self)
        self.widgets.extend([self.t_dato_end, self.t_dato_end_ent])
        self.ent.append(self.t_dato_end_ent)

        self.results = tk.Label(self, text="----")
        self.widgets.append(self.results)

        gt.pack_widgets(self.widgets)

        but = tk.Button(self, text='Søk til i database', width=25, command=self.get_from_db)
        self.widgets.append(but)

        log_button = tk.Button(self, text="Se logg", command=self.get_from_db)
        log_button.pack()

        home_button = tk.Button(self, text="Gå tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()


    def get_from_db(self):
        ovelse_navn = self.t_form_comb.get()
        ovelse_id = int(DB.project_table_where('ovelse_id', 'ovelse', 'navn', ovelse_navn))
        query_set, on_apparat = DB.ovelse_log_in_interval(ovelse_id, self.t_dato_start_ent.get(), self.t_dato_end_ent.get())
        print(query_set)
        string = ""
        if on_apparat:
            for element in query_set:
                string += f"---------------\n"
                string += f"Dato: {element[0]}\nNavn: {element[1]}\nAntall kilo: {element[2]}\nAntall sets: {element[3]}\n"

        else:
            for element in query_set:
                string += "----------------\n"
                string += f"Dato: {element[0]}\nNavn: {element[1]}\nBeskrivelse: {element[2]}\n"
        self.results.config(text=string)


class PersonalRecordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Din personlige rekord")
        label.pack(pady=10,padx=10)
        self.all_ovelse = DB.project_table('ovelse', 'navn')

        t_id = tk.Label(self, text="Øvelse")
        self.t_form_comb = ttk.Combobox(self, values=self.all_ovelse)
        self.t_form_comb.pack()

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10,padx=10)

        button = tk.Button(self, text="Hent fra database", command=self.getExercises)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()


    def getExercises(self):
        ex = DB.getPersonalRecord(self.t_form_comb.get())
        try:
            string= "Ant Kilo: " + str(ex[1]) + "\nAnt set:" + str(ex[2]) + "\nNavn: " + ex[3]
        except Exception:
            string = ex
        self.results.config(text=string)

class AddOvelseTreningsoktPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.all_ovelse = DB.project_table('ovelse', 'navn')
        self.all_treningsokt = DB.project_table('treningsokt', 'treningsokt_id, dato')

        self.title = tk.Label(self, text="Logg øvelse i treningsøkt")
        self.widgets.append(self.title)

        okt_id = tk.Label(self, text="Treningsøkt")
        self.okt_entry = ttk.Combobox(self, values=self.all_treningsokt)
        self.widgets.extend([okt_id, self.okt_entry])

        ovelse_id = tk.Label(self, text="Øvelse")
        self.ovelse_entry = ttk.Combobox(self, values=self.all_ovelse)
        self.widgets.extend([ovelse_id, self.ovelse_entry])

        button = tk.Button(self, text="Legg til øvelse i treningsøkt", command=self.into_db)


        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)

    def into_db(self):
        ovelse_navn = self.ovelse_entry.get()
        ovelse_id = int(DB.project_table_where('ovelse_id', 'ovelse', 'navn', ovelse_navn))
        print(ovelse_id)

        treningsokt_id = self.okt_entry.get().split(" ")[0]
        print(treningsokt_id)

        ovelse_treningsokt_relasjon = OvelseTreningsoktRelasjon(ovelse_id, treningsokt_id)
        ovelse_treningsokt_relasjon.save()
        self.title.config(text="Databasen har blitt oppdatert")
        #gt.empty_ent(self.ent)

#viktig mainloop


app = main()
app.mainloop()



