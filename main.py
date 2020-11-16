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
        for string in tmp_df.keys():
            if "Bewertung" in string:
                resultat = tmp_df['Bewertung/30,00'].reset_index(drop=True).to_string()[5:]

    print(nachname + ", " + vorname + ": " + resultat)
    print("--------------------------------------------------")
