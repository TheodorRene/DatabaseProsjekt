from pages import *


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