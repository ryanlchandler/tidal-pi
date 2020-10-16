import sys
import subprocess
import logging

logger = logging.getLogger(__name__)

def i2cdetect():
    try:
        result = subprocess.run(["i2cdetect", "-y", "1"], capture_output=True, shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except:
        logger.error("error running i2cdetect", sys.exc_info()[0])
        return "error running i2cdetect"






