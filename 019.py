# time cost = 6.46 ms ± 10.9 µs

import datetime as dt

def count_sundays():
    delta = dt.timedelta(days=1)
    start_date = dt.datetime(1901, 1, 1)
    end_date = dt.datetime(2000, 12, 31)
    count = 0
    while start_date <= end_date:
        if start_date.day==1 and start_date.isoweekday()==7: count+=1
        start_date += delta
    return count
