import re

from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'foo', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = [
    'yhttp >= 3.6.1',
    'yhttp-pony >= 2.4.0',
    'gunicorn',
]


setup(
    name='yhttp-boilerplate',
    version=package_version,
    packages=find_packages(exclude=['tests']),
    package_dir={'foo': 'foo'},
    install_requires=dependencies,
    license='',
    url='https://github.com/yhttp/yhttp-boilerplate',
    author='atipy',
)
