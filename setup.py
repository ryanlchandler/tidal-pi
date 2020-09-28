from setuptools import setup, find_packages
from glob import glob
from os.path import splitext
from os.path import basename

setup(
    name="TidalPi",
    version="0.1",
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    entry_points={
        'console_scripts': [
            'tidalpi = tidal_pi.app:start'
        ]
    }
)
