"""
	This programme assesses the accuracy of the computed coastlinedata.
	
	The process is done throgh visual inspection of the coastline data points and plotted
	coastlines from BaseMap module.

	The map is plotted specifically for East Asia.

	The name of the country in inspection in specified in country in PARAMETER
"""


# PARAMETER
# State the country to plot
country = 'Vietnam'



# LIBRARY IMPORT
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import json



# METHOD
# Set up plot figure
fig = plt.figure()

# Set up a basemap in East Asia region
map = Basemap(projection='cyl',llcrnrlat=0,urcrnrlat=60,\
            llcrnrlon=100,urcrnrlon=150,resolution='l')
# Draw parallels and meridians.
map.drawparallels(np.arange(0,60,10.))
map.drawmeridians(np.arange(100,150,10.))
map.drawcoastlines()
map.fillcontinents(color='coral',lake_color='aqua')
map.drawmapboundary(fill_color='aqua')

with open('%s' % country,'rb') as file:
    source = file.read()
    data = json.loads(source)

# Load the latitude and longitude data
latlon = data[1]

x = [item[0] for item in latlon]
y = [item[1] for item in latlon]

plt.plot(x,y, 'ko')
plt.title("Map of %s" % country)
plt.show()   