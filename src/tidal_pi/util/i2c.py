import sys
import subprocess
import logging

logger = logging.getLogger(__name__)

def i2cdetect():
    try:
        result = subprocess.run(['i2cdetect', '-y 1'], stdout=subprocess.PIPE)
        return result.stdout
    except:
        logger.error("error running i2cdetect", sys.exc_info()[0])
        return "error running i2cdetect"






