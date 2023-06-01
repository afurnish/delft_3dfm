from setuptools import find_packages, setup
setup(
    name='delft3dfm',
    packages=find_packages(include=['delft3dfm', 'xarray', 'numpy', 'pandas','easygui']),
    version='1.0.0',
    description='A suite of packages to help program the delft 3d flexible mesh suite, set up input files and generate models to run on supercomputers',
    author='Aaron Andrew Furnish',
    license='MIT',
)