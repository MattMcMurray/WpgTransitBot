from datetime import datetime, timedelta

from pytz import timezone


def get_wpg_time():
    wpg_tz = timezone('Canada/Central')
    wpg_time = datetime.now(wpg_tz)

    time_str = wpg_time.strftime('%Y-%m-%dT%H:%M:%S')

    return time_str
