from setuptools import setup

with open("docs/README.md", "r") as fh:
    long_description = fh.read()

with open("docs/LICENSE") as fh:
    LICENSE = fh.read()

setup(
    name="bsmLib",
    version="0.0.1",
    author="Andrew Voss",
    author_email="avoss19@bsmschool.org",
    description="Library for BSM Robotics",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    license=LICENSE,
    url="https://github.com/BSMRKRS/bsmLib/",
    packages=['bsmLib'],
    package_dir={'bsmLib': 'src/bsmLib'},
    install_requires=['pygame'],
    platforms=['any'],
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
