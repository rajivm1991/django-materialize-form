from setuptools import setup, find_packages
from materializeform.meta import VERSION

setup(
    name='django-materialize-form',
    version=str(VERSION),
    description="Django Materialize Form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=['materialize', 'django'],
    author='Rajiv Subramanian M',
    author_email='rajiv.m1991@gmail.com',
    url='http://github.com/rajivm1991/django-materialize-form',
    download_url='https://github.com/rajivm1991/django-materialize-form/tarball/0.1.1',
    install_requires=['Django', ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)
