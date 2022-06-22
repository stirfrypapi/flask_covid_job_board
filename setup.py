"""
job_board python package configuration.
"""

from setuptools import setup

setup(
    name='job_board',
    version='0.1.0',
    packages=['job_board'],
    include_package_data=True,
    install_requires=[
        'Flask==1.1.1',
        'requests==2.22.0',
        'pandas==1.0.3',
        'numpy==1.22.0',
        'us==1.0.0',
        'matplotlib==3.1.2'
    ],
)