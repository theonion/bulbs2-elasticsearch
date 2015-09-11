#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


version = "0.0.1"

name = "bulbs2-elasticsearch"
package = "bulbs2_elasticsearch"
description = "The Latest in Onion Technical Debt"
url = "https://github.com/theonion/bulbs2-elasticsearch"
author = "Vince Forgione"
author_email = "vforgione@theonion.com"
license = "MIT"

setup_requires = [
]

dev_requires = [
    "pytest",
    "pytest-django",
    "model_mommy",
]

install_requires = [
    "django>=1.8,<1.9",
    "djes",
]

server_requires = []

if "test" in sys.argv:
    setup_requires.extend(dev_requires)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["tests"]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=dev_requires,
    extras_require={
        "dev": dev_requires,
    },
    cmdclass={"test": PyTest}
)
