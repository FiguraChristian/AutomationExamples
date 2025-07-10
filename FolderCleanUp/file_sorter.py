# Modul-Import
import os
import shutil
import config
import pandas as pd

# Logging-Datei
log_file = "log.csv"

# Wenn Log-Datei nicht existiert, erstelle sie mit Spaltenüberschriften
if not os.path.isfile(log_file):
    df = pd.DataFrame(columns=['Dateiname', 'Alter Pfad', 'Neuer Pfad', 'Status'])
    df.to_csv(log_file, index=False)

# Logging-Funktion
def logging (dateiname, alter_pfad, neuer_pfad, status):
    new_entry = pd.DataFrame([{
        'Dateiname': dateiname,
        'Alter Pfad': alter_pfad,
        'Neuer Pfad': neuer_pfad,
        'Status': status
    }])

    # Anhängen an die bestehende CSV (ohne Header)
    new_entry.to_csv(log_file, mode='a', header=False, index=False)

# Ordner sortieren
def sort_folder(selected_path):
    # Sprung in das Zielverzeichnis und Auflistung des Inhalts
    files = os.listdir(selected_path)

    # Iteration über Dateien im Zielverzeichnis
    for file in files:
        file_path = os.path.join(selected_path, file)

        # Wenn es sich um ein file handelt, wird die Dateiendung extrahiert
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file.lower())[1]
            # Hier erfolgt der "match" mit dem Dictionary in der config.py
            zielordner = config.FOLDER_MAPPING.get(file_extension, config.DEFAULT_FOLDER)
            zielordner_pfad = os.path.join(selected_path, zielordner)

            os.makedirs(zielordner_pfad, exist_ok=True)

            try:
                neuer_pfad = os.path.join(zielordner_pfad, file)
                shutil.move(file_path, neuer_pfad)
                print(f"Die Datei '{file}' wurde in den Ordner '{zielordner}' verschoben")

                # Logging erfolgreicher Move
                logging(file, file_path, neuer_pfad, 'Erfolgreich')

            except Exception as e:
                print(f"Die Datei '{file}' konnte nicht verschoben werden. Fehler: {e}")

                # Logging bei Fehler
                logging(file, file_path, 'Fehler', f'Fehler: {e}')

