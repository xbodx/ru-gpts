from datetime import datetime, timedelta

'''
Returns a duration as specified by variable interval
Functions, except totalDuration, returns [quotient, remainder]
'''


def duration(delta: timedelta, interval="default"):
    delta_in_s = delta.total_seconds()

    def __get_duration_in_s(sec=None):
        return sec if sec != None else delta_in_s

    def years():
        return divmod(delta_in_s, 31536000)  # Seconds in a year=31536000.

    def days(sec=None):
        return divmod(__get_duration_in_s(sec), 86400)  # Seconds in a day = 86400

    def hours(sec=None):
        return divmod(__get_duration_in_s(sec), 3600)  # Seconds in an hour = 3600

    def minutes(sec=None):
        return divmod(__get_duration_in_s(sec), 60)  # Seconds in a minute = 60

    def seconds(sec=None):
        return divmod(__get_duration_in_s(sec), 1)

    def millisecond(sec=None):
        return divmod(1000 * __get_duration_in_s(sec), 1)

    def totalDuration():
        y = years()
        d = days(y[1])
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])
        n = millisecond(s[1])
        return f"{int(y[0])} years {int(d[0])} days {int(h[0])} hours {int(m[0])} mins {int(s[0])}.{int(n[0])} secs"

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()[0]),
        'millisecond': int(millisecond()[0]),
        'default': totalDuration()
    }[interval]


if __name__ == "__main__":
    start = datetime(2012, 3, 5, 23, 8, 15, 999999)
    finish = datetime(2020, 3, 5, 23, 8, 13, 111111)
    delta = finish - start
    print(duration(delta))
    print(f"years {duration(delta, 'years')}")
    print(f"days {duration(delta, 'days')}")
    print(f"hours {duration(delta, 'hours')}")
    print(f"minutes {duration(delta, 'minutes')}")
    print(f"seconds {duration(delta, 'seconds')}")
    print(f"millisecond {duration(delta, 'millisecond')}")
