import geopandas as gpd
from sqlalchemy import create_engine
import requests


def get_landkreise_gdf():
    """Query WFS service and return GeoDataFrame"""
    url = "https://sgx.geodatenzentrum.de/wfs_vg5000_0101"

    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typename": "vg5000_krs",
        "srsName": "EPSG:4326",
        "outputFormat": "application/json"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Create GeoDataFrame from GeoJSON
        gdf = gpd.GeoDataFrame.from_features(response.json(), crs="EPSG:4326")

        # Clean column names if needed
        gdf.columns = [col.lower() for col in gdf.columns]

        return gdf
    else:
        raise Exception(f"Request failed: {response.status_code}\n{response.text}")


def save_to_postgis(gdf, table_name, dbname, user, password, host='localhost', port=5432):
    """Save GeoDataFrame to PostGIS database"""
    # Create SQLAlchemy engine
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(conn_str)

    # Save to PostGIS
    gdf.to_postgis(
        table_name,
        engine,
        if_exists='replace',  # or 'append' for adding to existing table
        index=False,
        dtype={'geometry': 'GEOMETRY(GEOMETRY, 4326)'}
    )
    print(f"Successfully saved to PostGIS table {table_name}")


# Usage example
if __name__ == "__main__":
    # Get data from WFS
    landkreise_gdf = get_landkreise_gdf()

    # Inspect the data
    print(landkreise_gdf.head())
    print(f"CRS: {landkreise_gdf.crs}")

    # Save to PostGIS (adjust parameters for your database)
    save_to_postgis(
        landkreise_gdf,
        table_name="landkreise",
        dbname="your_database",
        user="admin",
        password="Passwort",
        host="your_host",
        port=5432
    )