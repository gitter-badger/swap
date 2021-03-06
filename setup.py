#!/usr/bin/env python3

from setuptools import setup, find_packages

import swap

# README.md
with open("README.md", "r") as readme:
    long_description = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="swap",
    version=swap.__version__,
    description="Cross-chain atomic swap between the networks of two Cryptocurrencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=swap.__license__,
    author=swap.__author__,
    author_email=swap.__email__,
    url="https://github.com/meherett/shuttle",
    packages=find_packages(),
    keywords=["cross-chain", "atomic", "swap", "htlc", "cryptocurrencies"],
    entry_points={
        "console_scripts": ["swap=swap.cli.__main__:main"]
    },
    python_requires=">=3.6,<4",
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=6.0.1,<7",
            "pytest-cov>=2.10.1,<3"
        ],
        "docs": [
            "sphinx>=3.2.1,<4",
            "sphinx_rtd_theme>=0.5.0,<1",
            "sphinx_click>=2.5.0,<3"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development"
    ],
)
