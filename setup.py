# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    ptest_args = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run(self):
        import pytest
        pytest.main(self.pytest_args)

setup(
    name='PyIEProxy',
    version='0.1.0',
    description='Python IE Proxy Switch',
    url='https://github.com/magichan-lab/pyieproxy',
    author='Magichan',
    author_email='magichan.lab@gmail.com',
    maintainer='Magichan',
    maintainer_email='magichan.lab@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["*.tests"]),
    install_requires=['wheel', 'requests'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ie-proxy = bin.command:main',
        ]},
    extras_require={
        'test': ['pytest-cov',
                 'pytest-pep8',
                 'coverage',
                 'pep8',
                 'pytest'],
        'docs': ['sphinx'],
    },
    cmdclass={'test': PyTest},
)
