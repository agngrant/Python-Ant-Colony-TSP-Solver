import csv
import sys
import ConfigParser

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def main(argv):
    print argv
    config = ConfigParser.RawConfigParser()
    config.read(argv[1])

    plt.figure(figsize=(config.getint('figure', 'width'), config.getint('figure', 'height')))
    map = Basemap(projection=config.get('map', 'projection'),
                  lat_0=config.getfloat('map', 'lat_0'), lon_0=config.getfloat('map', 'lon_0'),
                  resolution=config.get('map', 'resolution'), area_thresh=config.getfloat('map', 'area_thresh'),
                  llcrnrlon=config.getfloat('map', 'llcrnrlon'), llcrnrlat=config.getfloat('map', 'llcrnrlat'),
                  urcrnrlon=config.getfloat('map', 'urcrnrlon'), urcrnrlat=config.getfloat('map', 'urcrnrlat'))

    map.drawcoastlines()
    map.drawcountries()
    map.drawrivers(color='b')
    map.fillcontinents(color='green')
    map.drawmapboundary()

    csvfile = open(argv[0], 'rU')
    csvreader = csv.reader(csvfile)
    cities = {}

    for row in csvreader:
        cities[row[0]] = {'lat': float(row[1]), 'lon': float(row[2])}
    csvfile.close()

    lats = []
    lons = []
    path = []

    if len(argv) == 3:
        path = argv[2]
        for value in path:
            lats.append(cities[value]['lat'])
            lons.append(cities[value]['lon'])
        lats.append(cities[path[0]]['lat'])
        lons.append(cities[path[0]]['lon'])
        x, y = map(lons, lats)

        for label, xpt, ypt in zip(path, x, y):
            plt.text(xpt + 10000, ypt + 5000, label)

        map.plot(x, y, 'D-', markersize=10, linewidth=1, color='k', markerfacecolor='b')

        plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
