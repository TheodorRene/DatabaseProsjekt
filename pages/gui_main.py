from pages import *
from database import DB

class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        pages = [LandingPage, TreningsoktPage, LastNTrainingExercisesPage, ApparatPage, OvelsePage, RegisterOvelsegruppePage, AddOvelseToOvelsegruppePage, RetrieveOvelseInOvelsegruppePage, IntervallLoggPage,PersonalRecordPage,AddOvelseTreningsoktPage]
        for F in pages:
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(LandingPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = main()
app.mainloop()