import requests
import json

# API Base URL
BASE_URL = "https://www.wegweiser-kommune.de/data-api/rest"

# Indikator für PKW mit Elektroantrieb in Berlin
FRIENDLY_URL = "pkw-mit-elektroantrieb+ALLE+STAEDTE+2020-2022"

# Format für den Export
EXPORT_FORMAT = "json"

# Optionale Parameter
PARAMS = {
    "charset": "UTF-8",  # Zeichensatz setzen
    "download": "true"   # Datei als Download anbieten
}

# API Request URL
request_url = f"{BASE_URL}/export/{FRIENDLY_URL}.{EXPORT_FORMAT}"

# Anfrage senden
response = requests.get(request_url, params=PARAMS)

if response.status_code == 200:
    # JSON speichern
    filename = "elektro_pkw_alle_st_2020-2022.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
    print(f"Daten erfolgreich gespeichert: {filename}")

    # Optional: JSON laden und anzeigen
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print(f"Fehler: {response.status_code}", response.text)