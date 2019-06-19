from gmplot import gmplot
from data import data
from api_key import api_key
from os import path


def render_map(food, year, month):

    if year != None and month != None:
        lats = [view['location'][0] for view in data if view['food'] ==
                food and view['year'] == int(year) and view['month'] == int(month)]
        longs = [view['location'][1] for view in data if view['food'] ==
                 food and view['year'] == int(year) and view['month'] == int(month)]
    else:
        lats = [view['location'][0] for view in data if view['food'] == food]
        longs = [view['location'][1] for view in data if view['food'] == food]

    gmap = gmplot.GoogleMapPlotter(25, 0, 2)  # lat, long, zoom(default)
    gmap.scatter(lats, longs, 'red', size=150000, marker=False, alpha=1.0)

    gmap.apikey = api_key
    gmap.draw(path.join(path.dirname(path.abspath(__file__)), 'gmplot.html'))

    with open(path.join(path.dirname(path.abspath(__file__)), 'gmplot.html'), 'r+') as f:
        z = f.read()
        # updated zoom (2 -> 1.8)
        z = z.replace("zoom: 2", "zoom: 1.8")
        f.write(z)
