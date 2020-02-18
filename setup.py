#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name="flake8-os-walk",
    version="0.1.0",
    description="Flake8 plugin which usage of os.walk().",
    author="Asher Foa",
    author_email="asher@asherfoa.com",
    url="https://github.com/asherf/flake8-os-walk",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    keywords="flake8",
    entry_points={"flake8.extension": ["OW = flake8_os_walk:OSWalkChecker"]},
    install_requires=["flake8>=3.7"],
    tests_require=["coverage", "pytest"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Framework :: Flake8",
    ],
)
