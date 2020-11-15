import pandas as pd

df = pd.read_csv("eintragungsliste.csv")
list_of_names = []
for i in range(0, len(df)):
    string = df[df.keys()[1]].tolist()[i]
    last, first = string.split(',')
    list_of_names.append([last, first])

print(list_of_names)