try:
    from setuputils import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'C/C++ file concatenation',
    'author': 'Anthony Stathers',
    'url': 'https://github.com/ads2357/camalgamate',
    'author_email': 'astathers@gmail.com',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['camalgamate'],
    'name': 'camalgamate',
}

setup(**config)
