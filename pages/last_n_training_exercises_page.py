from pages import *


class LastNTrainingExercisesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.num_values = [1,2,3,4,5,6,7,8,9,10]

        label = tk.Label(self, text="Dine siste øvelser")
        label.pack(pady=10,padx=10)

        self.results = tk.Label(self, text="-------------------")
        self.results.pack(pady=10,padx=10)

        button = tk.Button(self, text="Hent fra database", command=self.getExercises)
        button.pack()

        home_button = tk.Button(self, text="Gå til tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

        self.num_ent = ttk.Combobox(self,values = self.num_values)
        self.num_ent.pack()

        #Nødvendig hvis vi må forholde oss til en person
        #self.pnr_ent = tk.Entry(self)
        #self.pnr_ent.pack()

    def getExercises(self):
        el = DB.get_n_okter(int(self.num_ent.get()))
        string=""
        for liste in el:
            string += "----------------\n"
            string += f"Dato: {liste[0]}\nVarighet: {liste[1]}\nPersonlig form:{liste[2]}\nPrestasjon:{liste[3]}\nTreningssenter: {liste[4]}\n"
        self.results.config(text=string)