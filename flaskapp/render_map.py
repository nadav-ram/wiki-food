from gmplot import gmplot
from data import data


def render_map(food):

    lats, longs = [], []

    for view in data:
        if view['food'] == food:
            lats.append(view['location'][0])
            longs.append(view['location'][1])

    gmap = gmplot.GoogleMapPlotter(25, 0, 2)
    gmap.scatter(lats, longs, 'red', size=150000, marker=False)

    gmap.draw('gmplot.html')

    # Replace "\" with "/" in the html file
    s = open('gmplot.html').read()
    s = s.replace("\\", "/")
    f = open('gmplot.html', 'w')
    f.write(s)
    f.close()
