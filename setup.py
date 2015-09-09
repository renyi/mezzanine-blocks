from setuptools import setup, find_packages

NAME = 'mezzanine-blocks'

VERSION = '0.9.2'

DESCRIPTION = """
A mezzanine flavored fork of django-flatblocks.
The goal of this project is to be able to easily create custom blocks of
text/HTML in the template, and can be editable via admin.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    version=VERSION,
    author='Renyi Khor',
    author_email='renyi.ace@gmail.com',
    url='https://github.com/renyi/mezzanine-blocks',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    requires=['mezzanine'],
)
