"""Setup file for data-structures repo."""
from setuptools import setup

setup(
    name="data-structures",
    description="Implementations of various data structures in Python",
    version=0.1,
    author="Matt Favoino",
    licence="MIT",
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}
)
