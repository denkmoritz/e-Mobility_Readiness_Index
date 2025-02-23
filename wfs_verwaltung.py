import requests

# WFS service URL
url = "https://sgx.geodatenzentrum.de/wfs_vg5000_0101"

# Parameters for the WFS GetFeature request
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typename": "vg5000_krs",  # Potential typename for Landkreise
    "srsName": "EPSG:4326",     # Coordinate system (WGS84)
    "outputFormat": "application/json"  # Request GeoJSON format
}

# Send the request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Retrieved {len(data['features'])} Landkreise")
    # Process the GeoJSON data here
    for feature in data["features"]:
        properties = feature["properties"]
        print(f"{properties.get('gen')} ({properties.get('bez')})")
else:
    print(f"Request failed with status {response.status_code}")
    print(response.text)

