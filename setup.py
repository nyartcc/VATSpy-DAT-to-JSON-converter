from setuptools import setup
setup(
    name='VATspy DATE to JSON converter',
    version='0.2.0',
    entry_points={
        'console_scripts': [
            'vatspy_dat_converter=vatspy_dat_converter:run'
        ]
    }
)