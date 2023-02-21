from setuptools import setup, find_packages

import imp

version = imp.load_source('jamsx.version', 'jamsx/version.py')

setup(
    name='jamsx',
    version=version.version,
    description='A JAMS extension to support audio and symbolic annotations.',
    author='JAMS-X development crew',
    url='https://github.com/smashub/jams-x',
    download_url='https://github.com/smashub/jams-x/releases',
    packages=find_packages(),
    package_data={'': ['schemata/*.json',
                       'schemata/namespaces/*.json',
                       'schemata/namespaces/*/*.json']},
    long_description='A JSON Annotated Music Specification for Reproducible MIR Research',
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    keywords='audio symbolic music json',
    license='ISC',
    install_requires=[
        'pandas',
        'sortedcontainers>=2.0.0',
        'pyrsistent<0.15; python_version=="3.4"',
        'jsonschema>=3.0.0',
        'numpy>=1.8.0',
        'six',
        'decorator',
        'mir_eval>=0.5',
    ],
    extras_require={
        'display': ['matplotlib>=1.5.0'],
        'tests': ['pytest < 4', 'pytest-cov'],
    },
    scripts=['scripts/jamsx_to_lab.py']
)
