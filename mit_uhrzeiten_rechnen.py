import datetime as dt
import logging
"""
Modul wird in log_trial genutzt
Enthält Beispiele für die Nutzung von Date und Datetime-Objekten
"""


print("__name__=",__name__)

def do_something():
    logger = logging.getLogger(__name__)
    print('>> MUR - Start')
    logger.info('in MUR')
    # Time-Objekt aus Integern für H, M und S erstellen
    rtc_time = dt.time(23,20,0)
    recentAlarm = dt.datetime.combine(dt.datetime.today(), rtc_time)
    # Verwendung von timedelta()
    nextAlarm = recentAlarm + dt.timedelta(minutes=15)
    # Beispiel für Formatierung
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    nextAlarm = recentAlarm + dt.timedelta(hours=1)
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    nextAlarm = recentAlarm + dt.timedelta(hours=2, minutes=30)
    logger.info('nextAlarm: ' + nextAlarm.strftime('%d.%m.%y'))
    print(">> MUR - Done")


if __name__=='__main__':
    do_something()