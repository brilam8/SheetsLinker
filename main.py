import tkinter as tk
from tkcalendar import Calendar, DateEntry

class Application():
    def __init__(self):
        self.create_widgets()

    def create_widgets(self):
        print("creating widgets...")
        window = tk.Tk()
        window.columnconfigure(0, weight=1, minsize=300)
        window.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=5)
        greeting = tk.Label(text="Welcome to the Sheets Linker!", font=('Ubuntu', 17))
        greeting.grid(row=0, column=0)

        comp = tk.Label(text="Company")
        comp.grid(row=1, column=0, sticky="sew", padx=(50, 50))
        nameEntry = tk.Entry(font=('Ubuntu', 12))
        nameEntry.grid(row=2, column=0, sticky="new", padx=(50, 50))


        pos = tk.Label(text="Position")
        titleEntry = tk.Entry(font=('Ubuntu', 12))
        pos.grid(row=3, column=0, sticky="sew", padx=(50, 50))
        titleEntry.grid(row=4, column=0, sticky="new", padx=(50, 50))

        linkLab = tk.Label(text="Link")
        linkEntry = tk.Entry(font=('Ubuntu', 12))
        linkLab.grid(row=5, column=0, sticky="sew", padx=(50, 50))
        linkEntry.grid(row=6, column=0, sticky="new", padx=(50, 50))

        dateAppLab = tk.Label(text="Date Applied")
        dateAppEntry = DateEntry(font=('Ubuntu', 12))
        dateAppLab.grid(row=7, column=0, sticky="sew", padx=(50, 50))
        dateAppEntry.grid(row=8, column=0, sticky="new", padx=(50, 50))

        button = tk.Button(text="Submit!")
        button.grid(row=9, column=0, sticky="new", padx=(50, 50), pady=(20, 20))

        def handle_apply(event):
            print("APPLIED")


        window.bind("<Return>", handle_apply)
        button.bind("<Button-1>", handle_apply)

        window.mainloop()

        

    
        

Application()