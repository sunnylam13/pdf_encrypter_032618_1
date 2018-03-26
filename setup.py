try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program goes through every PDF in a folder and its subfolders and encrypts the PDFs using a password provided on the command line.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PyPDF2,os,sys'],
	'scripts': [],
	'name': 'PDF Mass Encrypter'
}

setup(**config)