from pages import *


class ApparatPage(tk.Frame):
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
