from setuptools import setup, find_packages
setup(
    name="TidalPi",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tidalpi = tidal_pi.app:start'
        ]
    }
)
