from setuptools import setup
# py setup.py bdist_wheel
# twine upload dist/*
VERSION = '1.0.2'
AUTHOR = 'Hlight'
DESCRIPTION = 'Python library of IT Club PTIT HN'

setup(
    name='itptit',
    version=VERSION,
    url='https://github.com/hlighT-git/itptit',
    license='MIT',
    author=AUTHOR,
    author_email='hlight.mail@gmail.com',
    description=DESCRIPTION,
    package_dir={
        'itptit':'itptit',
        'itptit.common': 'itptit/common',
        'itptit.generator': 'itptit/generator',
        'itptit.judge': 'itptit/judge',
        'itptit.common.math': 'itptit/common/math',
        'itptit.common.random': 'itptit/common/random'
    },
    packages=[
        'itptit',
        'itptit.common',
        'itptit.generator',
        'itptit.judge',
        'itptit.common.math',
        'itptit.common.random'
    ],
    package_data={
        'itptit.common': ['*.pyi'],
        'itptit.generator': ['*.pyi'],
        'itptit.judge': ['*.pyi'],
        'itptit.common.math': ['*.pyi'],
        'itptit.common.random': ['*.pyi']
    },
    include_package_data = True,
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
