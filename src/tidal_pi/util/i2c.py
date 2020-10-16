import subprocess

def i2cdetect():
    result = subprocess.run(['i2cdetect', '-y 1'], stdout=subprocess.PIPE)
    return result.stdout



