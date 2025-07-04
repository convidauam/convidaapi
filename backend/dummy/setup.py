import os
from setuptools import setup, find_packages


setup(name='dummy',
      version=0.1,
      description='Example application',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['cornice', 'waitress'],
      entry_points="""\
      [paste.app_factory]
      main=dummy:main
      """,
      paster_plugins=['pyramid'])
