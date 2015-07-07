import urllib2
import StringIO

from xml.dom.minidom import parse
from secrets import TRANSIT_API_KEY
from time_adjust import get_wpg_time
from dateutil import parser


def __request_bus_times(stopnum, start_time, end_time):
    url = "http://api.winnipegtransit.com/v2/stops/{0}/schedule" .format(stopnum)
    url += '?start={0}&end={1}'.format(start_time, end_time)
    url += '&api-key={0}'.format(TRANSIT_API_KEY)

    try:
        xml_file = urllib2.urlopen(url)
        data = xml_file.read()

        dom = parse(StringIO.StringIO(data))
        xml_file.close()

        return dom

    except IOError as e:
        print (e)

        return None


def get_next_arrival(stopnum, routenum):
    start, end = get_wpg_time()
    dom = __request_bus_times(stopnum, start, end)
    next_arrival = None

    try:
        routes = dom.getElementsByTagName('route')

        for route in routes:
            key = route.firstChild.nextSibling
            if int(key.firstChild.data) == routenum:
                scheduled_stops = key.parentNode.nextSibling.nextSibling
                # this is ugly, but WpgTransit has a million nested items
                arrival = scheduled_stops.childNodes[1].childNodes[3].childNodes[1].childNodes[1].firstChild.data

                next_arrival = parser.parse(arrival)

    except Exception as e:
        print 'Something went wrong while parsing XML for stop schedule'
        print e.message

    return next_arrival
