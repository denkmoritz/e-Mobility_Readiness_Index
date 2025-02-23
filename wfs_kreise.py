import geopandas as gpd

# Define WFS URL and parameters
wfs_url = "https://sgx.geodatenzentrum.de/wfs_vg5000_0101"
layer_name = "vg5000_krs"  # Corrected layer name

# Construct the request URL for GeoJSON output
wfs_request_url = f"{wfs_url}?service=WFS&version=1.1.0&request=GetFeature&TYPENAME={layer_name}&outputFormat=application/json"

# Read the data into a GeoDataFrame
gdf = gpd.read_file(wfs_request_url)

# Display first rows
print(gdf.head())

# Plot all Kreise
gdf.plot(figsize=(10, 10), edgecolor="black", facecolor="lightblue")