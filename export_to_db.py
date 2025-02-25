import pandas as pd

names = {"e-auto_lk" : "/data/e-auto_landkreise.csv",
         "e-auto_st" : "/data/e-auto_staedte.csv",
         "lade_lk" : "/data/ladesaeulen_landkreise.csv",
         "lade_st" : "/data/ladesaeulen_staedte.csv",
         "strom_lk": "/data/strom_landkreise.csv",
         "strom_st" : "/data/strom_staedte.csv"
         }

for name, data in names.items():
    df = pd.read_csv(data)
    df.