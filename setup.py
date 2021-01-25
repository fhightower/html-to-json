#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = ['bs4']

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='html_to_json',
    version='1.0.7',
    description='Convert html to json.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Floyd Hightower',
    author_email='',
    url='https://github.com/fhightower/html_to_json',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=requirements,
    license='MIT License',
    zip_safe=True,
    keywords='html_to_json',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
