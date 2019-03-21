from pages import *


class AddOvelseToOvelsegruppePage(tk.Frame):
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


        #for el in self.widgets:
        #    el.pack()
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