import datetime as dt
import logging

print("__name__=",__name__)

def do_something():
    logger = logging.getLogger(__name__)
    print('>> MUR - Start')
    logger.info('in MUR')
    rtc_time = dt.time(23,20,0)
    recentAlarm = dt.datetime.combine(dt.datetime.today(), rtc_time)
    nextAlarm = recentAlarm + dt.timedelta(minutes=15)
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    nextAlarm = recentAlarm + dt.timedelta(hours=1)
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    nextAlarm = recentAlarm + dt.timedelta(hours=2, minutes=30)
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    print(">> MUR - Done")
