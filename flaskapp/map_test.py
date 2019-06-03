from gmplot import gmplot
from data import data

lats, longs = [], []

for view in data:
    lats.append(view['location'][0])

for view in data:
    longs.append(view['location'][1])

gmap = gmplot.GoogleMapPlotter(90, -90, 0)
gmap.scatter(lats, longs, 'red', size = 10)

gmap.apikey = 'AIzaSyD-FJQEw4YX1tIhTcN_fmkEe7BXzaxEAuE'
gmap.draw('gmplot.html')