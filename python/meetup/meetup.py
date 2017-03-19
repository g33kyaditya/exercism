import datetime
import calendar

class MeetupDayException(Exception):
    pass

def weekdayToNumber(day):
    if day == 'Monday':
        return 0;
    elif day == 'Tuesday':
        return 1
    elif day == 'Wednesday':
        return 2
    elif day == 'Thursday':
        return 3
    elif day == 'Friday':
        return 4
    elif day == 'Saturday':
        return 5
    elif day == 'Sunday':
        return 6
    else:
        pass

def meetup_day(year, month, day, status):
    si = [13, 14, 15, 16, 17, 18, 19]
    count = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, d) for d in range(1, count + 1)]

    if status == 'teenth':
        for d in days:
            if d.day in si and weekdayToNumber(day) == d.weekday():
                return d
    elif status == '1st' or status == '2nd' or status == '3rd' or status == '4th' or status == '5th':
        needed = int(status[0])
        for d in days:
            if weekdayToNumber(day) == d.weekday():
                needed = needed-1
            if needed == 0:
                return d
        raise MeetupDayException

    else:
        for d in reversed(days):
            if weekdayToNumber(day) == d.weekday():
                return d
