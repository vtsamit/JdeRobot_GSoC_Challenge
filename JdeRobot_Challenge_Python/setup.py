from setuptools import find_packages, setup

setup(
    name='BrownianMotion',
    packages=find_packages(include=['BrownianMotion']),
    version='1.0',
    description='Python Module',
    author='Me',
    install_requires=['numpy',
                      'pygame==2.5.2'],
)
