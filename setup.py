#setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test",
    version="0.0.1",
    author="zhangll",
    author_email="524631266@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a524631266/pypi_test.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)