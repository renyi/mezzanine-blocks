from setuptools import setup, find_packages

NAME = 'mezzanine-blocks'

VERSION = '0.9.4'

DESCRIPTION = """
A fork of https://github.com/molokov/mezzanine-blocks.git to make it work with Django 1.9
A mezzanine flavored fork of django-flatblocks.
The goal of this project is to be able to easily create custom blocks of
text/HTML in the template, and can be editable via admin.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    version=VERSION,
    author='Daverio Antony',
    author_email='contact@circonflex.fr',
    url='https://github.com/Cajoline/mezzanine-blocks',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
        requires=['mezzanine'],
        classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
