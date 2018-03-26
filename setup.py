try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program goes through every PDF in a folder and its subfolders and encrypts the PDFs using a password provided on the command line.  Also included is the reverse program which decrypts all encrypted pdfs with a provided password.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/pdf_encrypter_032618_1',
	'download_url': 'https://github.com/sunnylam13/pdf_encrypter_032618_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PyPDF2,os,sys'],
	'scripts': [],
	'name': 'PDF Mass Encrypter'
}

setup(**config)