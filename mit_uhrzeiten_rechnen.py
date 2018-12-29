import datetime as dt
import logging

print("__name__=",__name__)

def do_something():
    rtc_time = dt.time(23,20,0)
    recentAlarm = dt.datetime.combine(dt.datetime.today(), rtc_time)
    nextAlarm = recentAlarm + dt.timedelta(minutes=15)
    logging.info(nextAlarm)
    nextAlarm = recentAlarm + dt.timedelta(hours=1)
    logging.info(nextAlarm)
    nextAlarm = recentAlarm + dt.timedelta(hours=2, minutes=30)
    logging.info(nextAlarm)
    print("Done")
