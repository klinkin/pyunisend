"""
PyUniSend Python wrapper for API UniSender.com
-----------

Links
`````

* `UniSender API documentation <http://www.unisender.com/en/help/api>`_
* `PyUniSend source <http://github.com/klinkin/pyunisend>`_
"""

from setuptools import setup, find_packages
import pyunisend

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: Russian',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'unisender api wrapper'

setup(
    name = 'pyunisend',
    version = pyunisend.__version__,
    author = pyunisend.__author__,
    author_email = pyunisend.__author_email__,
    license = 'MIT license',
    description = 'Wrapper API UniSender.com for Python',
    long_description = __doc__,
    url = "https://github.com/klinkin/pyunisend",
    packages = find_packages(),
    download_url = "http://pypi.python.org/pypi/pyunisend/",
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    platforms = 'any',
    zip_safe = True,
    install_requires=['distribute']
)