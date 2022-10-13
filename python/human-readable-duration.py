
# Human readable duration format - 4 kyu
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

#  For seconds = 62, your function should return:
# "1 minute and 2 seconds"
# For seconds = 3662, your function should return:
# "1 hour, 1 minute and 2 seconds"
# https: // www.codewars.com/kata/52742f58faf5485cae000b9a/train/python for more details

def format_duration(seconds):
    if seconds == 0:
        return "now"
    # check for years
    elif seconds > 31535999:
        dys = seconds//86400
        yrs, rem_days = years(dys)
        format_plural(yrs, 'year')
        if rem_days > 0:
            format_plural(rem_days, 'day')
     # check for days
    elif seconds > 86399:
        hrs = seconds//3600
        dys, rem_hours = days(hrs)
        format_plural(dys, 'day')
        if rem_hours > 0:
            format_plural(rem_hours, 'hour')
    # check for hours
    elif seconds > 3599:
        mins = seconds//60
        hrs, rem_mins = hours(mins)
        format_plural(hrs, 'hour')
        if rem_mins > 0:
            format_plural(rem_mins, 'minute')
    # check for minutes
    elif seconds > 59:
        mins, rem_secs = minutes(seconds)
        format_plural(mins, 'minute')
        if rem_secs > 0:
            format_plural(rem_secs, 'second') 
    # check for seconds
    elif seconds < 60:
        format_plural(seconds, 'second')


def format_plural(count, time_unit):
    if count > 1:
        print(f'{count} {time_unit}s')
        return(f'{count} {time_unit}s')
    else:
        print(f'{count} {time_unit}')
        return(f'{count} {time_unit}')

def minutes(seconds):
    # 60 seconds per minute
    minutes = seconds//60
    rem_seconds = seconds%60
    return minutes, rem_seconds

def hours(minutes):
    # 60 minutes per hour
    # 3600 seconds per hour
    hours = minutes//60
    rem_minutes = minutes%60
    return hours, rem_minutes

def days(hours):
    # 24 hours per day
    # 1440 minutes per day
    # 86,400 seconds per day
    days = hours//24
    rem_hours = hours%24
    return days, rem_hours

def years(days):
    # 365 days per year
    # 8,760 hours per year
    # 525,600 minutes per year
    # 31,536,000 seconds per year
    years = days//365
    rem_days = days%365
    return years, rem_days

dur1 = 1
dur2 = 62
dur3 = 120
dur4 = 3600
dur5 = 3662

#format_duration(dur1)
#format_duration(2)
#format_duration(dur2)
#format_duration(dur3)
#format_duration(dur4)
#format_duration(dur5)
