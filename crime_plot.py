import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import descartes
from shapely.geometry import Point, Polygon
from mpl_toolkits.basemap import Basemap
import contextily as ctx
import folium
from IPython.display import HTML, display

df = pd.read_csv('./streetcrime.csv')

'''
mapCrimeColor = {
    'Violence and sexual offences':'red',\
    'Anti-social behaviour':'blue',\
    'Drugs':'green',\
    'Public order':'orange',\
    'Theft from the person':'yellow',\
    'Criminal damage and arson':'black',\
    'Possession of weapons':'pink',\
    'Vehicle crime':'purple',\
    'Bicycle theft':'purple',\
    'Shoplifting':'white',\
    'Burglary':'grey',\
    'Robbery':'grey',\
    'Other theft':'magenta',\
    'Other crime':'cyan'
}

# using an image of the UK
uk_map = plt.imread('./map.png')

BoundBox = (-6.00, -2.00, 49.95, 51.20)
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.Longitude, df.Latitude, zorder=1, alpha=0.3, c=df['Crime type'].apply(lambda x: mapCrimeColor[x]),s=10)

ax.set_title('Crime locations on a UK Map')
ax.set_xlim(BoundBox[0],BoundBox[1])
ax.set_ylim(BoundBox[2],BoundBox[3])

ax.imshow(uk_map, zorder=0, extent=BoundBox, aspect='equal')

# using an image of the Exeter Region
exe_map = plt.imread('./exe_map.png')

BoundBoxExe = (-3.58, -3.45, 50.68, 50.75)
fig2, ax2 = plt.subplots(figsize = (8,7))
ax2.scatter(df.Longitude, df.Latitude, zorder=1, alpha=0.5,c=df['Crime type'].apply(lambda x: mapCrimeColor[x]),s=10)

ax2.set_title('Crime locations on an Exeter Map')
ax2.set_xlim(BoundBoxExe[0],BoundBoxExe[1])
ax2.set_ylim(BoundBoxExe[2],BoundBoxExe[3])

ax2.imshow(exe_map, zorder=0, extent=BoundBoxExe, aspect='equal')
'''

def plot_gdf_folium(gdf, center):
    m = folium.Map(center, zoom_start=10, tiles='OpenStreetMap')
    folium.GeoJson(gdf).add_to(m)
    return m



# using a shape file showing vector boundaries
exe_shape_map = gpd.read_file('./Exeter_oa11.shp').to_crs(epsg=3857) #4326

BoundBoxExe3857 = (-398523.78, -384052.24, 6564883.44, 6577190.19) # EPSG:3857
crs = {'init':'epsg:4326'}
geometry = [Point(x,y) for x,y in zip(df['Longitude'], df['Latitude'])]
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry).to_crs(epsg=3857)



# street map shape file with crime points and ctx background map
fig3, ax3 = plt.subplots(figsize = (8,8))
geo_df.plot(ax = ax3,column='Crime type')
exe_shape_map.plot(ax = ax3, alpha = 0.1, color='grey')
#ctx.add_basemap(ax3)

#my_map = plot_gdf_folium(geo_df,[-3.45, 50.68])
my_map = folium.Map(location=[50.71984,-3.53019], zoom_start=10)
display(my_map)
'''
# metadata taken from epsg:3857 values
ax3.set_title('Crime locations on a shape file of Exeter')
ax3.set_xlim(BoundBoxExe3857[0],BoundBoxExe3857[1])
ax3.set_ylim(BoundBoxExe3857[2],BoundBoxExe3857[3])
'''
'''
geo_df[geo_df['Crime type'] == 'Violence and sexual offences'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Violence and Sexual Offences")
geo_df[geo_df['Crime type'] == 'Anti-social behaviour'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Anti-social behaviour")
geo_df[geo_df['Crime type'] == 'Drugs'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Drugs")
geo_df[geo_df['Crime type'] == 'Public order'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Public order")
geo_df[geo_df['Crime type'] == 'Theft from the person'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Theft from the person")
geo_df[geo_df['Crime type'] == 'Criminal damage and arson'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Criminal damage and arson")
geo_df[geo_df['Crime type'] == 'Possession of weapons'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Possession of weapons")
geo_df[geo_df['Crime type'] == 'Vehicle crime'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Vehicle crime")
geo_df[geo_df['Crime type'] == 'Bicycle theft'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Bicycle theft")
geo_df[geo_df['Crime type'] == 'Shoplifting'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Shoplifting")
geo_df[geo_df['Crime type'] == 'Burglary'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Burglary")
geo_df[geo_df['Crime type'] == 'Robbery'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Robbery")
geo_df[geo_df['Crime type'] == 'Other theft'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Other theft")
geo_df[geo_df['Crime type'] == 'Other crime'].plot(ax= ax3, markersize = 20, color = 'blue', marker='o', label="Other crime")
'''
plt.show()
