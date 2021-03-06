#!/usr/bin/env python
# encoding: utf-8
"""django-clippy provides a template tag for the Django Web Framework
to allow copying the Clipboard.

Functionality is implemented in Flash.

Read more at http://github.com/mdornseif/django-clippy#readme
"""

# setup.py
# Created by Maximillian Dornseif on 2009-07-19 for HUDORA.
# Copyright (c) 2009 HUDORA. All rights reserved.


from distutils.core import setup
setup(name='django-clippy',
      maintainer='Maximillian Dornseif',
      maintainer_email='md@hudora.de',
      version='1.1',
      url='http://github.com/mdornseif/django-clippy#readme',
      description='Flash based template tag for Django to allow copying the clipboard',
      long_description=__doc__,
      packages=['clippy', 'clippy.templatetags'],
      include_package_data=True,
      zip_safe=False,
      package_data={'clippy': ['static/clippy.swf']},
      install_requires=['Django'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: Implementation :: CPython',],
)
