from pages import *


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