import logger
import mit_uhrzeiten_rechnen as mur


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fH = logging.FileHandler("test_logger.log")
fH.setLevel(logging.DEBUG)

cH = logging.StreamHandler()
cH.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fH.setFormatter(formatter)
cH.setFormatter(formatter)

logger.addHandler(fH)
logger.addHandler(cH)

logger.info("erster Aufruf")
mur.do_something()
