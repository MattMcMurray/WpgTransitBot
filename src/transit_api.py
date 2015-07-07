import urllib2
from xml.dom.minidom import parse
import xml.dom.minidom
import StringIO

from secrets import TRANSIT_API_KEY


def request_bus_times(stop_id, start_time, end_time):
    url = "http://api.winnipegtransit.com/v2/stops/{0}/schedule" .format(stop_id)
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
