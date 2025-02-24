import requests

# API Base URL
BASE_URL = "https://www.wegweiser-kommune.de/data-api/rest"

list = ["LANDKREISE", "STAEDTE"]

for type in list:
    # Indikator für PKW mit Elektroantrieb in Berlin
    FRIENDLY_URL = f"pkw-mit-elektroantrieb+ALLE+{type}+2020-2021"

    # Format für den Export (CSV statt JSON)
    EXPORT_FORMAT = "csv"

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
        # CSV speichern
        filename = f"elektro_pkw_alle_{type}_2020-2022.csv"
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Daten erfolgreich als CSV gespeichert: {filename}")
    else:
        print(f"Fehler: {response.status_code}", response.text)