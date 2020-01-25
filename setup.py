from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name='text_processor',
    version='0.1',
    description='A simple module for basic text preprocessing.',
    long_description=readme,
    python_requires='>=3.6',
    packages=find_packages(exclude=('data')),
    install_requires=reqs.strip().split('\n'),
)
