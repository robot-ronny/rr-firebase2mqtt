from setuptools import setup, find_packages


NAME = 'firebase2mqtt'
DESCRIPTION = 'Bridge between Google Firebase RD and MQTT'
URL = 'https://github.com/robot-ronny/rr-firebase2mqtt'
EMAIL = '0radimkozak0@gmail.com'
AUTHOR = 'worepix'
VERSION = '0.0.1'
LICENSE = 'MIT'
CLASSIFIERS = [
        'Programming Language :: Python'
    ]
CONSOLE_SCRIPTS = ['firebase2mqtt=firebase2mqtt:main']


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    }
)
