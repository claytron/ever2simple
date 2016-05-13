from setuptools import setup, find_packages

version = '2.0'

setup(
    name='ever2simple',
    version=version,
    description=(
        "Migrate from evernote to simplenote with markdown formatting"),
    long_description=(
        open("README.rst").read() +
        '\n\n' +
        open("HISTORY.rst").read()
    ),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='note taking migration',
    author='Clayton Parker',
    author_email='robots@claytron.com',
    url='http://claytron.com',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        'python-dateutil<2.0',
        'html2text',
    ],
    entry_points="""
    [console_scripts]
    ever2simple = ever2simple.core:main
    """,
    )
