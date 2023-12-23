# Module for finding the wake hour and bed hour.

from datetime import datetime, date, time, timedelta, timezone

# start_day_time = datetime.strptime("05:00 am", '%I:%M %p')

# sleep_hours = timedelta(hours=8)

# routine_duration = timedelta(hours=2)

# wake_time = (start_day_time+routine_duration).strftime('%I:%M %p')
# bed_time = (datetime.strptime(wake_time, '%I:%M %p') -
#             sleep_hours).strftime('%I:%M %p')

# print(wake_time)
# print(bed_time)


def wake_and_bed(start_day_time: int, sleep_hours_int: int, routine_duration_int: int) -> dict:
    """
    Calculate the wake hour and bed hour based on the desired 
    start time and duration of the morning routine; and the desired sleep hours.

    Parameters:
    - start_day_time (int): the hour at which the morning routine will start in the format 'II:MM AM/PM'
    - sleep_hours (int): the desired hours of sleep.
    - routine_duration (int): the duration of the morning routine

    returns:
    - [wake_time (str),bed_time (str)] (dict)

    """
    # Validate inputs

    # Convert inputs
    # start_day_time = datetime.strptime(start_day_time_string, '%I:%M:%S %p')
    # Using an arbitrary date for calculation
    start_day_time = bedtime = datetime(2023, 1, 1, start_day_time, 0)
    sleep_hours = timedelta(hours=sleep_hours_int)
    routine_duration = timedelta(hours=routine_duration_int)

    # Calculate wake and bed time
    wake_time = start_day_time-routine_duration
    bed_time = wake_time - sleep_hours

    # Format outputs

    return {"wake time": wake_time.strftime('%I:%M:%S %p'), "bed time": bed_time.strftime('%I:%M:%S %p')}
