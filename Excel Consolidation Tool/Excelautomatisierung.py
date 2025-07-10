
# Modulimport
import os
import pandas as pd

# Zielordner definieren
projekt_ordner = "C:\\Users\\cfigura\\OneDrive - COMPUTACENTER\\Documents\\Projektordner"

# Auflistung Dateien Zielordner
files = os.listdir(projekt_ordner)

# Name der zu extrahierenden Spalten (könnte per Userabfrage und / oder GUI erfolgen)
spalten_zum_extrahieren = ["Projekt-ID", "Status","Bearbeiter","Letztes Update"]

# Der Name der Ausgabedatei, in die alle Daten zusammengeführt werden
# Kalenderwoche könnte um eine Userabfrage und / oder GUI erweitert werden
ausgabedatei = "projektstatus_kw27.xlsx"

# Leere Liste für den Inhalt der files, als Art Sammelbehälter zur Zwischenspeicherung
eingelesene_daten = []


## Daten einlesen

# Iteration über Dateien im Zielordner
for file in files:
    # Zielordner auf Exceldateien durchsuchen
    if file.endswith(".xlsx"):
        # Nur Projektdateien suchen
        if file.startswith("projekt"):
            # Dateipfad ermitteln
            filepath = os.path.join(projekt_ordner, file)

            try:
                # Inhalt der Dateien wird in ein DataFrame geladen
                df = pd.read_excel(filepath)

                # gewünschte Spalten könnten per Userabfrage und / oder GUI abgefragt werden
                extrahiertes_df = df[spalten_zum_extrahieren]

                # Füge das extrahierte DataFrame zur Liste hinzu
                eingelesene_daten.append(extrahiertes_df)


            # FileNotFoundError nicht ausreichend, da Files z.B. auch geöffnet sein könnten
            except Exception as e:
                print(f"FEHLER: Konnte Datei '{file}' nicht lesen oder verarbeiten. Grund: {e}")


## Daten zusammenführen und speichern

# nur, wenn Daten erfasst und zwischengespeichert wurden
if eingelesene_daten:
    # Daten zusammenführen und
    # sicherstellen, dass Die Daten fortlaufend sortiert sind (Neuaufbau des Index)
    final_df = pd.concat(eingelesene_daten, ignore_index=True)

    # Zielpfad der neuen Exceldatei definieren
    output_filepath = os.path.join(projekt_ordner, ausgabedatei)

    try:
        # Das zusammengeführte DataFrame in eine neue Excel-Datei speichern
        # 'index=False' verhindert, dass Pandas den neuen DataFrame-Index als zusätzliche Spalte speichert
        # somit wird alles um eine Spalte nach links geschoben
        final_df.to_excel(output_filepath, index=False)
        print(f"\nAlle Daten wurden erfolgreich in '{ausgabedatei}' zusammengeführt und gespeichert!")

    # File könnte z.B. auf einem Netzlaufwerk liegen und kann nicht erreicht werden
    except Exception as e:
        print(f"\nFEHLER: Konnte die Ausgabedatei '{ausgabedatei}' nicht speichern. Grund: {e}")
    else:
        print(
            "\nEs wurden keine passenden 'projekt'-Excel-Dateien gefunden oder geladen. Es wird keine Ausgabedatei erstellt.")






