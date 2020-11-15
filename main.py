import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("pandas")
import pandas as pd

# #######################################################################################################
# ONLY NEED TO DO THIS ONCE.
# #######################################################################################################
# Instructions:
# 1. Go to https://moseskonto.tu-berlin.de/moses/teilleistungen/
# 2. Navigate to Teilleistungsverwaltung
# 3. Choose the course, e.g.: Analysis I und Lineare Algebra für Ingenieurwissenschaften
# 4. Click "Teilleistungsergebnisse der Veranstaltung bearbeiten"
# 5. Under "Bitte wählen Sie die anzuzeigende(n) Teilleistung(en):", select HA0. It does not really matter, we just need
# any homework assignment. A new selection option should pop up: "Bitte wählen Sie die anzuzeigenden Studierenden:"
# 6. Select "Alle Studierenden aus meinen Tutorien"
# 7. Scroll to the bottom.
# 8. Click "Gespeicherte Ergebnisse als CSV Datei"
# 9. Download the CSV file and save it in the same folder as this file ("main.py"). This is important, name it:
# "eintragungsliste.csv"
# The apostrophes are NOT part of the filename.
# 10. You now have a CSV file with the names of your students in it.


# #######################################################################################################
# THIS NEEDS TO BE DONE FOR EVERY NEW HOMEWORK ASSIGNMENT.
# #######################################################################################################
# 1. Next, download the Online Hausaufgaben results from isis. Again, as a csv file. Save the results as "ha.csv"
# Put the file "ha.csv" in the same folder as this python repository.
# 2. Run this file. If you want to do it via commandline, navigate to this repo and execute the command python3 main.py
# 3. The console should now output the results of your students in a clean fashion. You no longer have to go through
# the entire list manually.

df = pd.read_csv("eintragungsliste.csv")
students = []
for i in range(0, len(df)):
    string = df[df.keys()[1]].tolist()[i]
    last, first = string.split(',')
    first = first[1:]
    students.append([last, first])
df = pd.read_csv("ha.csv")
for student in students:
    nachname = student[0]
    vorname = student[1]

    tmp_df = df[df["Nachname"] == nachname]
    # If multiple people with the same last name exist, check first name.
    # print(nachname, vorname)
    if len(tmp_df) == 0:
        resultat = "00,00"
    else:
        if len(tmp_df) > 1:
            tmp_df = tmp_df[tmp_df["Vorname"] == vorname]
            assert len(tmp_df) == 1, "There are two students with the same name."
        resultat = tmp_df['Bewertung/30,00'].reset_index(drop=True).to_string()[5:]

    print(nachname + ", " + vorname + ": " + resultat)
    print("--------------------------------------------------")
