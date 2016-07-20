try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'SMS-Slack relayer',
    'author': 'Matt Holford',
    'author_email': 'mholford@dosomething.org',
    'version': '0.0.1',
    'install_requires': ['Flask', 'nose'],
    'packages': ['sms_slack', 'flask_cors'],
    'scripts': [],
    'name': 'SMS-Slack'
}

setup(**config)