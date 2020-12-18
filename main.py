# Copyright <2020> <Elias Wirth, email: wirth@zib.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pandas")
import pandas as pd


def find(s, other):
    return s.find(other) != -1


df_students = pd.read_csv("students_list.csv")
df_students.sort_values("Name")

students = []
for i in range(0, len(df_students)):
    email = df_students["E-Mail"][i]
    vorname = df_students["Vorname"][i]
    nachname = df_students["Name"][i]
    students.append([email, vorname, nachname])

df = pd.read_csv("ha.csv")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Automatically Checking Online Exercises.")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(" ")
print("--------------------------------------------------")
for student in students:
    email = student[0]
    vorname = student[1]
    nachname = student[2]
    tmp_df = df[df["E-Mail-Adresse"] == email]
    if len(tmp_df) == 0:
        tmp_df = df[df["Nachname"] == nachname]

    if len(tmp_df) == 0:
        tmp_df = df[df["Vorname"] == vorname]

    if len(tmp_df) == 0:
        resultat = "00,00"
    else:
        if len(tmp_df) > 1:
            tmp_df = tmp_df[tmp_df["Vorname"] == vorname]
            tmp_df = tmp_df[tmp_df["Nachname"] == nachname]
            if len(tmp_df) == 0:
                resultat = "00,00"
            else:
                assert len(tmp_df) == 1, "There are two students with the same name."
        for string in tmp_df.keys():
            if "Bewertung" in string:
                resultat = tmp_df[string].reset_index(drop=True).to_string()[5:]

    print(nachname + ", " + vorname + ": " + resultat)
    print("--------------------------------------------------")
