from setuptools import setup, find_packages

setup(
    name='pydelhi',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'python-dateutil'
    ]
)