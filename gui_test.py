#! /usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tables import *
from database import DB
from functions import GuiTools as gt

#https://pythonprogramming.net/change-show-new-frame-tkinter/

class main(tk.Tk):
    '''
    Main function that runs the program
    '''
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        pages = [LandingPage, TreningsoktPage, LastNTrainingExercisesPage, ApparatPage, OvelsePage, RegisterOvelsegruppePage, AddOvelseToOvelsegruppePage, RetrieveOvelseInOvelsegruppePage, IntervallLoggPage, PersonalRecordPage, AddOvelseTreningsoktPage]
        for F in pages:
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(LandingPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LandingPage(tk.Frame):
    '''
    Front page for the application
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Exersiceboi")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Ny treningsøkt", command=lambda: controller.show_frame(TreningsoktPage))
        button.pack()

        button2 = tk.Button(self, text="Treningsøkter", command=lambda: controller.show_frame(LastNTrainingExercisesPage))
        button2.pack()

        button3 = tk.Button(self, text="Apparater",command=lambda: controller.show_frame(ApparatPage))
        button3.pack()

        button4 = tk.Button(self, text="Registrer øvelse",command=lambda: controller.show_frame(OvelsePage))
        button4.pack()

        button5 = tk.Button(self, text="Registrer gruppeøvelse", command=lambda: controller.show_frame(RegisterOvelsegruppePage))
        button5.pack()

        button6=tk.Button(self, text="Legg øvelse til gruppeøvelse", command=lambda: controller.show_frame(AddOvelseToOvelsegruppePage))
        button6.pack()

        button7 = tk.Button(self, text="Finn øvelser i gruppeøvelse", command=lambda: controller.show_frame(RetrieveOvelseInOvelsegruppePage))
        button7.pack()

        button8 = tk.Button(self, text="Intervallogg", command=lambda: controller.show_frame(IntervallLoggPage))
        button8.pack()

        button9 = tk.Button(self, text="Personlig rekord", command=lambda: controller.show_frame(PersonalRecordPage))
        button9.pack()

        button10 = tk.Button(self, text="Legg til øvelse i økt", command=lambda: controller.show_frame(AddOvelseTreningsoktPage))
        button10.pack()

class TreningsoktPage(tk.Frame):
    '''Page for creating new treningsokts'''
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

        # Adds all widgets
        for el in self.widgets:
            el.pack()

        home_button = tk.Button(self, text="Gå tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()


    def into_db(self):
        okt = Treningsokt(*[el.get() for el in self.ent])
        okt.save()
        self.title.config(text="Databasen har blitt oppdatert")


class LastNTrainingExercisesPage(tk.Frame):
    '''
    Page for showing the last 'n' treningokts, n given by the user.
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.num_values = [1,2,3,4,5,6,7,8,9,10]

        label = tk.Label(self, text="Dine siste øvelser")
        label.pack(pady=10,padx=10)

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10,padx=10)

        button = tk.Button(self, text="Hent fra database", command=self.get_exercises)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

        self.num_ent = ttk.Combobox(self,values = self.num_values)
        self.num_ent.pack()

    def get_exercises(self):
        el = DB.get_n_okter(int(self.num_ent.get()))
        string=""
        for liste in el:
            string += "----------------\n"
            string += f"Dato: {liste[0]}\nVarighet: {liste[1]}\nPersonlig form:{liste[2]}\nPrestasjon:{liste[3]}\nTreningssenter: {liste[4]}\n"
        self.results.config(text=string)


class OvelsePage(tk.Frame):
    '''
    Page for registering a new ovelse
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.all_apparat = DB.project_table('apparat', 'navn')

        self.title = tk.Label(self, text="Registrer øvelse med apparat")
        self.widgets.append(self.title)

        ov_id = tk.Label(self, text="Ovelse id")
        self.ov_id_ent = tk.Entry(self)
        self.widgets.extend([ov_id, self.ov_id_ent])

        ov_navn = tk.Label(self, text="Navn på øvelse")
        self.ov_navn_ent = tk.Entry(self)
        self.widgets.extend([ov_navn, self.ov_navn_ent])

        ov_kilo = tk.Label(self, text="Antall kilo")
        self.ov_kilo_ent = tk.Entry(self)
        self.widgets.extend([ov_kilo, self.ov_kilo_ent])

        ov_set = tk.Label(self, text="Antall set")
        self.ov_set_ent = tk.Entry(self)
        self.widgets.extend([ov_set, self.ov_set_ent])

        ov_ap_id = tk.Label(self, text="Apparat")
        self.apparat_entry = ttk.Combobox(self, values=self.all_apparat)
        self.widgets.extend([ov_ap_id, self.apparat_entry])

        button = tk.Button(self, text="Legg til i database", command=self.into_db)

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)

    def into_db(self):
        apparat_navn = self.apparat_entry.get()
        apparat_id = int(DB.project_table_where('apparat_id', 'apparat', 'navn', apparat_navn))

        ovelse = Ovelse(self.ov_id_ent.get(),self.ov_navn_ent.get())
        apparat_ovelse_relasjon = ApparatOvelseRelasjon(apparat_id,self.ov_id_ent.get())
        ovelse.save()
        apparat_ovelse_relasjon.save()
        ovelse_pa_apparat = Ovelse_pa_apparat(self.ov_id_ent.get(),self.ov_kilo_ent.get(),\
                                              self.ov_set_ent.get())
        ovelse_pa_apparat.save()
        self.title.config(text="Databasen har blitt oppdatert")
        #gt.empty_ent(self.ent)

class ApparatPage(tk.Frame):
    '''
    Page for creating a new apparat
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []

        self.title = tk.Label(self, text="Legg til apparat")
        self.widgets.append(self.title)

        ap_id = tk.Label(self, text="Apparat id")
        ap_id_ent = tk.Entry(self)
        self.widgets.extend([ap_id, ap_id_ent])
        self.ent.append(ap_id_ent)

        ap_navn = tk.Label(self, text="Navn")
        ap_navn_ent = tk.Entry(self)
        self.widgets.extend([ap_navn, ap_navn_ent])
        self.ent.append(ap_navn_ent)

        ap_beskrivelse = tk.Label(self, text="Beskrivelse")
        ap_beskrivelse_ent = tk.Entry(self)
        self.widgets.extend([ap_beskrivelse, ap_beskrivelse_ent])
        self.ent.append(ap_beskrivelse_ent)

        #for el in self.widgets:
        #    el.pack()
        gt.pack_widgets(self.widgets)

        button = tk.Button(self, text="Legg til i database", command=self.into_db)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

    def into_db(self):
        okt = Apparat(*[el.get() for el in self.ent])
        okt.save()
        self.title.config(text="Databasen har blitt oppdatert")
        gt.empty_ent(self.ent)

class RegisterOvelsegruppePage(tk.Frame):
    '''
    Page for registering a new ovelsegruppe
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []

        self.title = tk.Label(self, text="Registrer gruppeøvelse")
        self.widgets.append(self.title)

        ov_id = tk.Label(self, text="Ovelsegruppe id")
        self.ov_id_ent = tk.Entry(self)
        self.widgets.extend([ov_id, self.ov_id_ent])

        ov_navn = tk.Label(self, text="Navn på gruppeøvelse")
        self.ov_navn_ent = tk.Entry(self)
        self.widgets.extend([ov_navn, self.ov_navn_ent])

        button = tk.Button(self, text="Legg til i database", command=self.into_db)

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)

    def into_db(self):
        ovelsegruppe = Ovelsegruppe(self.ov_id_ent.get(),self.ov_navn_ent.get())
        ovelsegruppe.save()
        self.title.config(text="Databasen har blitt oppdatert")
        #gt.empty_ent(self.ent)

class AddOvelseToOvelsegruppePage(tk.Frame):
    '''
    Page for adding an ovelse to a ovelsegruppe
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []
        self.all_ovelsegruppe = DB.project_table('ovelsegruppe', 'navn')
        self.all_ovelse = DB.project_table('ovelse', 'navn')

        self.title = tk.Label(self, text="Legg til ovelse til ovelsegruppe")
        self.widgets.append(self.title)

        ovelsegruppe = tk.Label(self, text="Ovelsegruppe")
        self.ovelsegruppe_entry = ttk.Combobox(self, values=self.all_ovelsegruppe)
        self.widgets.extend([ovelsegruppe, self.ovelsegruppe_entry])
        self.ent.append(self.ovelsegruppe_entry)

        ovelse = tk.Label(self, text="Ovelse")
        self.ovelse_entry = ttk.Combobox(self, values=self.all_ovelse)
        self.widgets.extend([ovelse, self.ovelse_entry])
        self.ent.append(self.ovelse_entry)

        gt.pack_widgets(self.widgets)

        button = tk.Button(self, text="Legg til i ovelsegruppe", command=self.into_db)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

    def into_db(self):
        ovelse_navn = self.ovelse_entry.get()
        ovelse_id = int(DB.project_table_where('ovelse_id', 'ovelse', 'navn', ovelse_navn))

        ovelsegruppe_navn = self.ovelsegruppe_entry.get()
        ovelsegruppe_id = int(DB.project_table_where('ovelsegruppe_id', 'ovelsegruppe', 'navn', ovelsegruppe_navn))

        ovelse_i_ovelsegruppe = Ovelse_i_ovelsegruppe(ovelse_id,ovelsegruppe_id)
        ovelse_i_ovelsegruppe.save()
        self.title.config(text="Databasen har blitt oppdatert")
        gt.empty_ent(self.ent)


class RetrieveOvelseInOvelsegruppePage(tk.Frame):
    '''
    Page for showing all ovelses in a given ovelsegruppe
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.widgets = []
        self.ovelsegrupper = [el[0] for el in DB.project_table('ovelsegruppe', 'navn,ovelsegruppe_id')]

        self.title = tk.Label(self, text="Velg ovelsegruppe")
        self.widgets.append(self.title)

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10, padx=10)

        self.name_ent = ttk.Combobox(self, values=self.ovelsegrupper)
        self.name_ent.pack()

        button = tk.Button(self, text="Hent fra database", command=self.get_ovelser)

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)

    def get_ovelser(self):
        navn = self.name_ent.get()
        ovelsegruppe_id = DB.project_table_where('ovelsegruppe_id', 'ovelsegruppe', 'navn', navn)
        ovelsegrupper=DB.get_ovelser_in_ovelsegruppe(ovelsegruppe_id)
        string = "Ovelser:\n"
        for liste in ovelsegrupper:
            string += f"{liste}\n"
        self.results.config(text=string)


class IntervallLoggPage(tk.Frame):
    '''
    Page for showing treningokt history of a single ovelse in a specific time period.
    '''
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
    '''
    Page for showing the personal record. This is kind of arbitrary as the ovelses contains information about sets and weights..
    '''
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
        ex = DB.get_personal_record(self.t_form_comb.get())
        try:
            string= "Ant Kilo: " + str(ex[1]) + "\nAnt set:" + str(ex[2]) + "\nNavn: " + ex[3]
        except Exception:
            string = ex
        self.results.config(text=string)

class AddOvelseTreningsoktPage(tk.Frame):
    '''
    Page for adding a ovelse to a treningsokt.
    '''
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

        treningsokt_id = self.okt_entry.get().split(" ")[0]

        ovelse_treningsokt_relasjon = OvelseTreningsoktRelasjon(ovelse_id, treningsokt_id)
        ovelse_treningsokt_relasjon.save()
        self.title.config(text="Databasen har blitt oppdatert")


# RUNS THE SCRIPT
app = main()
app.mainloop()




