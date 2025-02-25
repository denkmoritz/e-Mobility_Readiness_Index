import geopandas as gpd
from sqlalchemy import create_engine

engine = create_engine("postgresql://docker:docker@localhost:25432/gis")

path = r"data/gadm41_DEU_2.json"

gdf = gpd.read_file(path)

gdf_cl = gdf[["NAME_1","NAME_2", "CC_2", "geometry"]]
gdf_cl.to_postgis("LK_geom", engine)



