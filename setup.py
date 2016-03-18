#!/usr/bin/env python

import os
import re
import sys
import codecs

from setuptools import setup, find_packages


# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv or 'develop' in sys.argv:
    os.chdir('socialaggregator')
    try:
        from django.core import management
        management.call_command('compilemessages', stdout=sys.stderr, verbosity=1)
    except ImportError:
        if 'sdist' in sys.argv:
            raise
    finally:
        os.chdir('..')


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='fluentcms-socialaggregator',
    version=find_version('socialaggregator', '__init__.py'),
    license='AGPL License',

    install_requires=[
        # 'twitter',
        'pytz',
        'django-filer'
        'django-taggit',
        # 'python-instagram',
        # 'google-api-python-client',
        # 'facebook-sdk',
        # 'feedparser',
    ],
    requires=[
        'Django (>=1.4)',
    ],

    description='Django app for aggregate some feeds from social networks.',
    long_description=read('README.rst'),

    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',

    url='https://github.com/bashu/fluentcms-socialaggregator',
    download_url='https://github.com/bashu/fluentcms-socialaggregator/zipball/master',

    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
