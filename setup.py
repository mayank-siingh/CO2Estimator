from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='co2Estimator',
    version='0.1.0',
    packages=['co2_estimator',],
    license='MIT license'
)
