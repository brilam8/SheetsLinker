import tkinter as tk
import json
from tkcalendar import Calendar, DateEntry
import heapq as hp
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('./config/client_secret.json')
client = gspread.authorize(creds)
sheet = client.open("Internships").sheet1

autoData = []
data = {}
with open("./config/auto.json") as f:
    data = json.load(f)

autoData = [(-value, key) for key, value in data.items()]
hp.heapify(autoData)
class Application():
    
    def __init__(self):
        with open("./config/row.json") as f:
            self.row = json.load(f)
        self.create_widgets()

    def create_widgets(self):
        more_variables_here = 0
        THIS_IS_A_NAME = "name here"
        very_useful_variable_1 = 1
        window = tk.Tk()
        window.title("Sheet Linker")
        window.columnconfigure(0, weight=1, minsize=300)
        window.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=5)
        greeting = tk.Label(text="Welcome to the Sheets Linker!", font=('Ubuntu', 16))
        greeting.grid(row=0, column=0)

        auto = tk.StringVar()
        nameText = tk.StringVar()
        linkText = tk.StringVar()
        rowText = tk.StringVar()

        comp = tk.Label(text="Company")
        comp.grid(row=1, column=0, sticky="sew", padx=(50, 50))
        nameEntry = tk.Entry(font=('Ubuntu', 12), textvariable=nameText)
        nameEntry.grid(row=2, column=0, sticky="new", padx=(50, 50))

        pos = tk.Label(text="Position")
        titleEntry = tk.Entry(font=('Ubuntu', 12), textvariable=auto)
        pos.grid(row=3, column=0, sticky="sew", padx=(50, 50))
        titleEntry.grid(row=4, column=0, sticky="new", padx=(50, 50))
        auto.set(autoData[0][1])

        linkLab = tk.Label(text="Link")
        linkEntry = tk.Entry(font=('Ubuntu', 12), textvariable=linkText)
        linkLab.grid(row=5, column=0, sticky="sew", padx=(50, 50))
        linkEntry.grid(row=6, column=0, sticky="new", padx=(50, 50))

        dateAppLab = tk.Label(text="Date Applied")
        dateAppEntry = DateEntry(font=('Ubuntu', 12))
        dateAppLab.grid(row=7, column=0, sticky="sew", padx=(50, 50))
        dateAppEntry.grid(row=8, column=0, sticky="new", padx=(50, 50))

        button = tk.Button(text="Submit!")
        button.grid(row=9, column=0, sticky="new", padx=(50, 50), pady=(20, 0))
        rowLab = tk.Label(font=('Ubuntu', 8), textvariable=rowText)
        rowText.set("Row: %d" % self.row["row"])
        rowLab.grid(row=10, column=0, sticky="new", padx=(50, 50), pady=(0, 20))
        

        
        def handle_apply(event):
            global autoData
            if (nameEntry.get().strip() == "" or titleEntry.get().strip() == "" or linkEntry.get().strip() == "" or dateAppEntry.get().strip() == ""):
                print("A field is empty")
            else:
                compName = nameEntry.get()
                linkName = linkEntry.get()
                date = dateAppEntry.get()
                titleName = titleEntry.get()
                entireString = "=HYPERLINK(\"" + linkName + "\",\"" + titleName + "\")"
                
                # Reset fields
                nameText.set("")
                linkText.set("")
                auto.set(autoData[0][1])


                # Update heap and JSON file
                if not titleName in data:
                    data[titleName] = 0
                data[titleName] = data[titleName] + 1
                autoData = [(-value, key) for key, value in data.items()] 
                with open("./config/auto.json", 'w') as json_file:
                    json.dump(data, json_file)
                hp.heapify(autoData)

                self.row["row"] += 1
                rowText.set("Row: %d" % self.row["row"])
                with open("./config/row.json", 'w') as row_file:
                    json.dump(self.row, row_file)
                sheet.update_cell(self.row["row"], 1, compName)
                sheet.update_cell(self.row["row"], 2, entireString)
                sheet.update_cell(self.row["row"], 3, date)
                
                
                

        def match_string():
            hits = []
            got = auto.get()
            for item in autoData:
                if item[1].lower().startswith(got.lower()):
                    hits.append(item[1])
            return hits

        def get_typed(event):
            if len(event.keysym) == 1:
                hits = match_string()
                show_hit(hits)

        def show_hit(lst):
            if len(lst) == 1:
                auto.set(lst[0])
                detect_pressed.filled = True

        def detect_pressed(event):    
            key = event.keysym
            if len(key) == 1 and detect_pressed.filled is True:
                pos = titleEntry.index(tk.INSERT)
                titleEntry.delete(pos, tk.END)
                

        detect_pressed.filled = False

        titleEntry.bind('<KeyRelease>', get_typed)
        titleEntry.bind('<Key>', detect_pressed)
        window.bind("<Return>", handle_apply)
        button.bind("<Button-1>", handle_apply)

        window.mainloop()

Application()