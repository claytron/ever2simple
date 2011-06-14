from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='ever2simple',
      version=version,
      description="Migrate from evernote to simplenote with markdown formatting",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='note taking migration',
      author='Clayton Parker',
      author_email='robots@claytron.com',
      url='http://claytron.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
