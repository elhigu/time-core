from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]

tests_require = [
    "nose"
]

setup(name='bookingcore',
    version=version,
    description="Advanced resource allocation engine.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='booking reservation timetable',
    author='Mikael Lepist\xc3\xb6',
    author_email='elhigu@gmail.com',
    url='possibly in github',
    license='BSD Use as you wish',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite = 'nose.collector',
    entry_points={
        'console_scripts':
            ['bookingcore=bookingcore:main']
    }
)
