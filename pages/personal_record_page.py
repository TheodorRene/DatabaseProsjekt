from pages import *


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