try:
	from setuptools import setup
except ImportError:
	from distutils.core improt setup

config = {
	'description': 'skeleton',
	'author': 'ipdae',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'qooraven@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['skeleton'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
