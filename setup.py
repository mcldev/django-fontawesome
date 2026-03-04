import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fontawesome',
    version='1.1',
    packages=['fontawesome'],
    include_package_data=True,
    license='BSD License',
    description='a django app that provides a couple of fontawesome/django related utilities.',
    long_description=README,
    url='https://www.github.com/redouane/django-fontawesome',
    author='Redouane Zait',
    author_email='redouanezait@gmail.com',
    install_requires=['PyYAML', 'Django>=4.2,<5.0'],
    python_requires='>=3.9',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Utilities',
    ],
)
