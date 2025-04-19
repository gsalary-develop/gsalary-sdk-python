from setuptools import setup, find_packages

setup(
    name='gsalary_sdk',
    version='0.0.1',
    author='Astro',
    author_email='astro.dai@globalfreepay.com',
    url='https://github.com/gsalary-develop/gsalary-sdk-python',
    packages=['clients'],
    description='gsalary python sdk',
    install_requires=['cryptography']
)