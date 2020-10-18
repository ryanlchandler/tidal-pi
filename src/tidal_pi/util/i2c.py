import sys
import subprocess
import logging

logger = logging.getLogger(__name__)

def i2cdetect():
    try:
        result = subprocess.run(["/usr/sbin/i2cdetect -y 1"], capture_output=True, shell=True)
        if result.returncode == 0:
            return result.stdout.decode("utf-8")
        else:
            return result.stderr.decode("utf-8")
    except:
        logger.error("error running i2cdetect", exc_info=True)
        return "error running i2cdetect"






