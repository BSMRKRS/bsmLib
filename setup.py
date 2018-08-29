from setuptools import setup

setup(
    name="bsmLib",
    version="0.0.1",
    author="Andrew Voss",
    author_email="avoss19@bsmschool.org",
    description="Library for BSM Robotics",
    long_description=open('docs/README.md').read(),
    license=open('docs/LICENSE').read(),
    url="https://github.com/BSMRKRS/bsmLib/",
    packages=['bsmLib'],
    package_dir={'bsmLib': 'src/bsmLib'},
    install_requires=['pygame', 'Serial'],
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
