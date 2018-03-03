from distutils.core import setup

setup(
    name='silent',
    version='0.1',
    packages=['silent'],
    url='',
    license='GPLv3',
    author='Vinyas N S',
    author_email='vinyasns@gmail.com',
    description='A commandline client for file.io',
    install_requires=['clint', 'python-magic', 'requests_toolbelt']
)
