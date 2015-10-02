import urllib2
import StringIO

from xml.dom.minidom import parse
from time_adjust import get_wpg_time
from dateutil import parser
from services import printlog
from keyWrapper import getKeyObj


# to get all arrival times, leave 'route' as None
def __request_bus_times(stop, route, start_time, end_time):
    url = "http://api.winnipegtransit.com/v2/stops/{0}/schedule?" .format(stop)

    if start_time is not None and end_time is not None:
        url += 'start={0}&end={1}&'.format(start_time, end_time)
    if route is not None:
        url += 'route={0}&'.format(route)
    url += 'api-key={0}'.format(getKeyObj().wpg_transit_key)

    print url

    try:
        xml_file = urllib2.urlopen(url)
        data = xml_file.read()

        dom = parse(StringIO.StringIO(data))
        xml_file.close()

        return dom

    except IOError as e:
        printlog("IOError while requesting bus times")
        printlog(e.message)

        return None


def get_next_arrival(stopnum, routenum):
    start, end = get_wpg_time()
    dom = __request_bus_times(stopnum, routenum, start, end)
    next_arrival = None
    
    try:
        estimated_arrivals = dom.getElementsByTagName('estimated')

        arrival = estimated_arrivals[0].firstChild.data
        next_arrival = parser.parse(arrival)

    except Exception as e:
        printlog('Something went wrong while parsing XML for stop schedule')
        printlog(e.message)

    return next_arrival
