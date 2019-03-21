from pages import *


class IntervallLoggPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.widgets = []
        self.ent = []
        self.all_ovelse = DB.project_table('ovelse', 'navn')

        self.title = tk.Label(self, text="Se intervallogg")
        self.widgets.append(self.title)

        t_id = tk.Label(self, text="Øvelse")
        self.t_form_comb = ttk.Combobox(self, values=self.all_ovelse)
        self.widgets.extend([t_id,self.t_form_comb])
        self.ent.append(self.t_form_comb)

        #dato start
        self.t_dato_start = tk.Label(self, text="Intervall start: (YYYY-MM-DD")
        self.t_dato_start_ent = tk.Entry(self)
        self.widgets.extend([self.t_dato_start,self.t_dato_start_ent])
        self.ent.append(self.t_dato_start_ent)

        # dato end
        self.t_dato_end = tk.Label(self, text="Intervall slutt: (YYYY-MM-DD")
        self.t_dato_end_ent = tk.Entry(self)
        self.widgets.extend([self.t_dato_end, self.t_dato_end_ent])
        self.ent.append(self.t_dato_end_ent)

        self.results = tk.Label(self, text="----")
        self.widgets.append(self.results)

        gt.pack_widgets(self.widgets)

        but = tk.Button(self, text='Søk til i database', width=25, command=self.get_from_db)
        self.widgets.append(but)

        log_button = tk.Button(self, text="Se logg", command=self.get_from_db)
        log_button.pack()

        home_button = tk.Button(self, text="Gå tilbake", command=lambda: controller.show_frame(LandingPage))
        home_button.pack()

    def get_from_db(self):
        ovelse_navn = self.t_form_comb.get()
        ovelse_id = int(DB.project_table_where('ovelse_id', 'ovelse', 'navn', ovelse_navn))
        query_set, on_apparat = DB.ovelse_log_in_interval(ovelse_id, self.t_dato_start_ent.get(), self.t_dato_end_ent.get())
        print(query_set)
        string = ""
        if on_apparat:
            for element in query_set:
                string += f"---------------\n"
                string += f"Dato: {element[0]}\nNavn: {element[1]}\nAntall kilo: {element[2]}\nAntall sets: {element[3]}\n"

        else:
            for element in query_set:
                string += "----------------\n"
                string += f"Dato: {element[0]}\nNavn: {element[1]}\nBeskrivelse: {element[2]}\n"
        self.results.config(text=string)