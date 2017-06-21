from __future__ import unicode_literals
from setuptools import setup, find_packages

import refresh_token

setup(
    name='refresh_token',
    description='Do not use unless you know what you are doing! '
                'Adds an endpoint to reddit to generate refresh tokens for arbitrary users.',
    version=refresh_token.__version__,
    license='BSD 3 Clause',
    author='MIT Office of Digital Learning',
    author_email='mitx-devops@mit.edu',
    keywords='reddit',
    packages=find_packages(),
    install_requires=['r2'],
    entry_points={
        'r2.plugin':
            ['refresh_token = refresh_token:RefreshToken']
    },
    include_package_data=True,
    zip_safe=False,
)
