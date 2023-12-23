# Module for finding the wake hour and bed hour.

from datetime import datetime, date, time, timedelta, timezone


# inputs

# This is when you need to leave
# for work. It’s when your morning routine needs to end.
# start_time = datetime.strptime("05:00 am", '%I:%M %p')

# sleep_hours = timedelta(hours=8)

# routine_duration = timedelta(hours=2)

# wake_time = (start_time+routine_duration).strftime('%I:%M %p')
# bed_time = (datetime.strptime(wake_time, '%I:%M %p') -
#             sleep_hours).strftime('%I:%M %p')

# print(wake_time)
# print(bed_time)


def wake_and_bed(start_time: str, sleep_hours: int, routine_duration: int) -> list:
    """
    Calculate the wake hour and bed hour based on the desired 
    start time and duration of the morning routine; and the desired sleep hours.

    Parameters:
    - start_time (str): the hour at which the morning routine will start in the format 'II:MM AM/PM'
    - sleep_hours (int): the desired hours of sleep.
    - routine_duration (int): the duration of the morning routine

    returns:
    - [wake_time (str),bed_time (str)] (list)

    """

    return []
