"""
Setup for swagger-wtforms.

Generate wtform classes dynamically from swagger definition specifications.
"""

import os

from setuptools import setup

SRCDIR = '.'
folder = os.path.abspath(os.path.dirname(__file__))
test_requirements = [
    'Flask==0.10.1',
    'Flask-WTF==0.12',
    'pytest==3.0',
    'pytest-cov==2.4',
    'pyquery==1.2',
    'itsdangerous==0.24',
    'Jinja2==2.8',
    'MarkupSafe==0.23',
    'Werkzeug==0.11.10',
]
requirements = [
    'faker',
]

setup(
    name='type_mappers',
    version='0.0.1',
    description=('Map primitive types to various context specific uses.'),
    long_description=__doc__,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    url='https://github.com/christabor/type_mappers',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require=test_requirements,
    install_requires=requirements,
    extras_require={
        'sqlalch': ['sqlalchemy'],
        'factoryboy': ['factory-boy'],
        'wtforms': ['WTForms'],
    },
    package_dir={'type_mappers': 'type_mappers'},
    packages=['type_mappers'],
    zip_safe=False,
    include_package_data=True,
)
