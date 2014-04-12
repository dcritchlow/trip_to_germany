try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Trip to Germany',
    'author': 'Darin Critchlow',
    'url': 'https://github.com/dcritchlow/trip_to_germany',
    'download_url': 'https://github.com/dcritchlow/trip_to_germany',
    'author_email': 'darin@darincritchlow.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['GERMANY'],
    'scripts': [],
    'name': 'trip_to_germany'
}

setup(**config)
