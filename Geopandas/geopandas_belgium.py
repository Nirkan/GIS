import geopandas as gpd
import matplotlib.pyplot as plt

# Importing and plotting the cities shapefile
cities = gpd.read_file('belgian_cities.shp')
cities.plot(cmap = 'jet', column= 'NAME_4', figsize = (10, 10))
#plt.show()

# Imporing and plotting AOI shapefile
AOI = gpd.read_file('area_of_interest_.shp')
AOI.plot()
#plt.show()

# Display both shapefiles together 

fig, ax = plt.subplots(1)
cities.plot(ax=ax, cmap = 'rainbow')
AOI.plot(ax = ax, facecolor = 'yellow')
#plt.show()


# Intersection 

cities_in_AOI = gpd.overlay(cities, AOI, how = 'intersection')
cities_in_AOI.plot(figsize = (10, 10), cmap = 'jet', column = 'NAME_4')
plt.show()


# Area

cities_in_AOI['Area(km2)'] = cities_in_AOI.area/10**6
print(cities_in_AOI['Area(km2)'])


# Save the geodataframe to a .shp shapefile
cities_in_AOI.to_file('intersected_cities.shp')
