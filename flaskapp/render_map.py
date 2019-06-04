from gmplot import gmplot
from data import data
from api_key import api_key


def render_map(food):

    lats, longs = [], []

    for view in data:
        if view['food'] == food:
            lats.append(view['location'][0])
            longs.append(view['location'][1])

    gmap = gmplot.GoogleMapPlotter(25, 0, 2)  # lat, long, zoom(default)
    gmap.scatter(lats, longs, 'red', size=150000, marker=False, alpha=1.0)

    gmap.apikey = api_key
    gmap.draw('gmplot.html')

    z = open('gmplot.html').read()
    # THIS IS THE UPDATED ZOOM!! (CURRENTLY 1.8)
    z = z.replace("zoom: 2", "zoom: 1.8")
    f = open('gmplot.html', 'w')
    f.write(z)
    f.close()
