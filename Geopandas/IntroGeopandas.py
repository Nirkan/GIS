import geopandas as gpd
import matplotlib.pyplot as plt


# Importing an ESRI Shapefile and Plotting it using GeoPandas.
districts = gpd.read_file('Shapefiles/districts.shp')
#districts.plot(cmap = 'hsv', edgecolor = 'black', column = 'district')
#plt.show()

area_of_interest = gpd.read_file('Shapefiles/area_of_interest.shp')
#area_of_interest.plot()
#plt.show()

atms = gpd.read_file('Shapefiles/atms.shp')


# Plot the figure side by side
# fig, (ax1, ax2) = plt.subplots(nrows=2, figsize = (10, 8))
# districts.plot(ax = ax1, cmap = 'hsv', edgecolor = 'black', column = 'district' )
# area_of_interest.plot(ax = ax2, color = 'green')
# plt.show()


# Plotting multiple layers
# fig, ax = plt.subplots(figsize = (10, 8))
# districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district' )
# area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
# atms.plot(ax = ax, color = 'black', markersize = 25)
# plt.show()

# Reprojecting GeoPandas GeoDataFrames
fig, ax = plt.subplots(figsize = (8, 6))
districts = districts.to_crs(epsg = 32629)
districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district' )
area_of_interest = area_of_interest.to_crs(epsg = 32629)
area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
plt.show()


# Intersecting layers
districts_in_aoi = gpd.overlay(districts, area_of_interest, how = 'intersection')
districts_in_aoi.plot(edgecolor = 'red')
plt.show()

# Calculating the areas of the intersected layer.
districts_in_aoi['area'] = districts_in_aoi.area/1000000

# Exporting GeoPandas GeoDataFrames into an ESRI Shapefile
districts_in_aoi.to_file('districts_within_aoi.shp', driver = "ESRI Shapefile")
