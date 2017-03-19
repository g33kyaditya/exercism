from datetime import datetime, timedelta

def add_gigasecond(obj):
    foo = timedelta(seconds=10**9)
    ret = obj + foo
    return ret
