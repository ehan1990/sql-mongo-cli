import setuptools
from setuptools import setup


with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()


setup(
    name='sql-mongo-cli',
    version="1.0.0",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'smc = smc.cli:cli'
        ]
    }
)
