from pages import *


class RegisterOvelsegruppePage(tk.Frame):
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
