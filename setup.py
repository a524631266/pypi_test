#setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
# setuptools.find_packages(exclude=['contrib', 'docs']) packages=,["test","test.module1"]
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
    entry_points={
        'console_scripts':[
            'test1=pypi_test.module1:runcmd'
        ]
    }
)