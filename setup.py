import re
from os.path import join, dirname

from setuptools import setup, find_namespace_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'yhttp/boilerplate/__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = [
    'yhttp >= 6.3, < 7'
]


setup(
    name='boilerplate',
    version=package_version,
    install_requires=dependencies,
    license='',
    url='https://github.com/yhttp/yhttp-boilerplate',
    author='atipy',
    packages=find_namespace_packages(
        where='.',
        include=['yhttp.boilerplate'],
        exclude=['tests']
    ),
    entry_points={
        'console_scripts': [
            'yhttp-boilerplate = yhttp.boilerplate:app.climain'
        ]
    },
)
