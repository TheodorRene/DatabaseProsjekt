from pages import *


class TreningsoktPage(tk.Frame):
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
