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
        'Flask==2.3.2',
        'requests==2.22.0',
        'pandas==1.0.3',
        'numpy==1.18.2',
        'us==1.0.0',
        'matplotlib==3.1.2'
    ],
)