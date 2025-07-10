
# Hauptmodul importieren
import tkinter as tk

# Submodule installieren
from tkinter import ttk, filedialog, messagebox


# Import Funktion
from file_sorter import sort_folder

# Ein neues Tkinter-Objetzt erzeugen
root = tk.Tk()

# Titel festlegen
root.title("File Manager")

# Fenstergröße definieren
root.geometry("400x400")

# Spalte 0 anoassungsfähig machen
root.columnconfigure(0, weight=1)

# Ein Label erzeugen und platzieren
label = ttk.Label(root, text="Ordner aufräumen mit Tkinter")
label.grid(padx=10, pady=100)

# Platzhalter für späteren Pfad
selected_path = ""

# Funktion Ordnerauswahl durch User
def ordner_auswaehlen():
    global selected_path
    ordner = filedialog.askdirectory(title="Ordner auswählen")
    if ordner:
        selected_path = ordner
        print("Ausgewählter Ordner:", ordner)
        messagebox.showinfo("Ordner ausgewählt", f"Ordner: {ordner}")

# Funktion Bereinigung des Zielordners
def start_sorting():
    if selected_path:
        sort_folder(selected_path)
        messagebox.showinfo("Fertig", "Der Ordner wurde erfolgreich sortiert!")
    else:
        messagebox.showwarning("Kein Ordner ausgewählt", "Bitte zuerst einen Ordner auswählen!")

# Button für Ordnerauswahl erstellen und platzieren
button_label = ttk.Button(root, text="Ordner auswählen", command=ordner_auswaehlen)
button_label.grid(columnspan=2)

# Button für Ausführung und platzieren
start_button = ttk.Button(root, text="Start!", command=start_sorting)
start_button.grid(columnspan=2, pady=10)

# Loop, damit Fenster offen bleibt
root.mainloop()
