from pages import *


class OvelsePage(tk.Frame):
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

        ov_ap_id = tk.Label(self, text="Apparat id")
        self.apparat_entry = ttk.Combobox(self, values=self.all_apparat)
        self.widgets.extend([ov_ap_id, self.apparat_entry])

        button = tk.Button(self, text="Legg til i database", command=self.into_db)

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        self.widgets.extend([button, home_button])

        gt.pack_widgets(self.widgets)

    def into_db(self):
        apparat_navn = self.apparat_entry.get()
        apparat_id = int(DB.project_table_where('apparat_id', 'apparat', 'navn', apparat_navn))

        ovelse = Ovelse(self.ov_id_ent.get(), self.ov_navn_ent.get())
        apparat_ovelse_relasjon = ApparatOvelseRelasjon(apparat_id, self.ov_id_ent.get())
        print(apparat_ovelse_relasjon)
        ovelse.save()
        apparat_ovelse_relasjon.save()
        ovelse_pa_apparat = Ovelse_pa_apparat(self.ov_id_ent.get(), self.ov_kilo_ent.get(), \
                                              self.ov_set_ent.get())
        ovelse_pa_apparat.save()
        self.title.config(text="Databasen har blitt oppdatert")
        # gt.empty_ent(self.ent)