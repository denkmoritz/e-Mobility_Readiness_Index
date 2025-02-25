import pandas as pd

files_lk = ['strom-aus-erneuerbaren-quellen_alle_LANDKREISE_2020-2021.csv']

column_names = ["Name", "ID", "unknown_2", "Bundesland", "2020", "2021"]
columns_to_remove = ["unknown_2"]

for file in files_lk:
    df = pd.read_csv(file, sep=';', skiprows=4, skipfooter=10, engine='python', header=None, names=column_names, dtype={"ID": str})

    # Remove unwanted columns
    df = df.drop(columns=columns_to_remove)

    # Keep only the first six characters of the 'ID' column
    df["ID"] = df["ID"].str[:6]

    # Save the cleaned dataframe
    df.to_csv("strom_landkreise.csv", sep=';', index=False)