import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Sobhan Kumar Lenka",
    author_email="sobhanlenka@gmail.com",
    description="Bot in a different flavour",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sobhanlenka/optimus",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)