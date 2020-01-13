import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import descartes
from shapely.geometry import Point, Polygon
from mpl_toolkits.basemap import Basemap

df = pd.read_csv('./streetcrime.csv')


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

# using a shape file showing streets
'''
base_map = Basemap(llcrnrlon=BoundBoxExe[0],llcrnrlat=BoundBoxExe[2],urcrnrlon=BoundBoxExe[1], urcrnrlat=BoundBoxExe[3],resolution='i',projection='tmerc',lat_0=BoundBoxExe[0],lon_0=BoundBoxExe[2])
base_map.drawmapboundary(fill_color='aqua')
base_map.fillcontinents(color='#ddaa66',lake_color='aqua')
base_map.drawcoastlines()

base_map.readshapefile('./Exeter_lsoa11', 'Exeter_lsoa11')'''

street_map = gpd.read_file('./Exeter_lsoa11.shp')

crs = {'init':'epsg:4326'}
geometry = [Point(x,y) for x,y in zip(df['Longitude'], df['Latitude'])]

geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)

fig3, ax3 = plt.subplots(figsize = (8,8))
street_map.plot(ax = ax3, alpha = 0.4, color='grey')


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

plt.show()
