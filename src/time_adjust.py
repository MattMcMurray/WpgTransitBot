from datetime import datetime, timedelta

from pytz import timezone

TIME_BETWEEN = 1


def get_wpg_time():
    wpg_tz = timezone('Canada/Central')
    wpg_time_start = datetime.now(wpg_tz)
    wpg_time_end = wpg_time_start + timedelta(hours=TIME_BETWEEN)

    time_str_start = wpg_time_start.strftime('%Y-%m-%dT%H:%M:%S')
    time_str_end = wpg_time_end.strftime('%Y-%m-%dT%H:%M:%S')

    return time_str_start, time_str_end
