# Module for finding the wake hour and bed hour.

from datetime import datetime, date, time, timedelta, timezone


# inputs

# This is when you need to leave 
# for work. It’s when your morning routine needs to end.
start_time = datetime.strptime("05:00 am", '%I:%M %p')

sleep_hours = timedelta(hours=8)

routine_duration = timedelta(hours=2)

wake_time = (start_time+routine_duration).strftime('%I:%M %p')
bed_time = (datetime.strptime(wake_time,'%I:%M %p')-sleep_hours).strftime('%I:%M %p')

print(wake_time)
print(bed_time)

def wake_and_bed():
    # above logic
    return []