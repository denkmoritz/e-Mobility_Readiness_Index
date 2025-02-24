import pandas as pd

files_lk = ['ladesaeuleninfrastruktur_alle_LANDKREISE_2020-2021.csv']

column_names = ["Name", "unknown_1", "unknown_2", "Bundesland","2020", "2021"]
columns_to_remove = ["unknown_1", "unknown_2"]

for file in files_lk:
    df = pd.read_csv(file, sep=';', skiprows=4, skipfooter=10, engine='python', header=None, names=column_names)
    df = df.drop(columns=columns_to_remove)
    df.to_csv("ladesaeulen_landkreise.csv", sep=';', index=False)