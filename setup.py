from distutils.core import setup
from setuptools import find_packages

setup(
    name='ConstantContactLib',
    version='0.1.1',
    author='Dmitry Veretelnikov',
    author_email='dmitryveretelnikov@outlook.com',
    packages=find_packages(),
    url='https://github.com/dmitry1119/ConstantContactLib',
    license='LICENSE.txt',
    description='Constant Contact API Client',
    long_description=open('README.txt').read(),
    install_requires=[
        "oauth2 >= 1.5.211",
        "certifi >= 0.0.8",
        "httplib2 >= 0.9.2"
    ],
)
