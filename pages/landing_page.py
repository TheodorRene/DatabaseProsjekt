from pages import *

class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Exersiceboi")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Ny treningsøkt", command=lambda: controller.show_frame(TreningsoktPage))
        button.pack()

        button2 = tk.Button(self, text="Treningsøkter",command=lambda: controller.show_frame(Last_N_TrainingExercisesPage))
        button2.pack()

        button3 = tk.Button(self, text="Apparater",command=lambda: controller.show_frame(ApparatPage))
        button3.pack()

        button4 = tk.Button(self, text="Registrer øvelse",command=lambda: controller.show_frame(OvelsePage))
        button4.pack()

        button5 = tk.Button(self, text="Registrer gruppeøvelse", command=lambda: controller.show_frame(RegisterOvelsegruppePage))
        button5.pack()

        button6 = tk.Button(self, text="Legg øvelse til gruppeøvelse", command=lambda: controller.show_frame(AddOvelseToOvelsegruppePage))
        button6.pack()

        button7 = tk.Button(self, text="Finn øvelser i gruppeøvelse", command=lambda: controller.show_frame(RetrieveOvelseInOvelsegruppePage))
        button7.pack()

        button8 = tk.Button(self, text="Intervallogg", command=lambda: controller.show_frame(IntervallLoggPage))
        button8.pack()

        button9 = tk.Button(self, text="Personlig rekord", command=lambda: controller.show_frame(PersonalRecordPage))
        button9.pack()

        button10 = tk.Button(self, text="Legg til øvelse i økt", command=lambda: controller.show_frame(AddOvelseTreningsoktPage))
        button10.pack()