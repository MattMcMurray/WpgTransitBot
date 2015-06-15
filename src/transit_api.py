import urllib2
import xmltodict
import datetime

from secrets import TRANSIT_API_KEY

def request_bus_times(stop_id):
    datetime = datetime.datetime.now()
    url = "http://api.winnipegtransit.com/v2/stops/{0}/schedule?api-key={1}" .format(stop_id, TRANSIT_API_KEY)

    file = urllib2.urlopen(url)
    data = file.read()
    file.close()

    data = xmltodict.parse(data)

    return data