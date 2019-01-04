import logging
import mit_uhrzeiten_rechnen as mur
"""Beispiel für einen komlexeren Logger mit File- und Stream-Handler"""

print('>> Logger initialisieren')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fH = logging.FileHandler("test_logger.log")
fH.setLevel(logging.INFO)

cH = logging.StreamHandler()
cH.setLevel(logging.DEBUG)

print('>> Logger Formatierung')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fH.setFormatter(formatter)
cH.setFormatter(formatter)

print('>> Logger AddHandler')
logger.addHandler(fH)
logger.addHandler(cH)

logger.debug("nur im Debugging Modus")
logger.info("erster Aufruf")
mur.do_something()
