#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['bs4']

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='html_to_json',
    version='1.0.8',
    description='Convert html to json.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Floyd Hightower',
    author_email='',
    url='https://github.com/fhightower/html-to-json',
    project_urls={
        'Documentation': 'https://github.com/fhightower/html-to-json',
        'Say Thanks!': 'https://saythanks.io/to/floyd.hightower27%40gmail.com',
        'Source': 'https://github.com/fhightower/html-to-json',
        'Tracker': 'https://github.com/fhightower/html-to-json/issues',
        'PyPi': 'https://pypi.org/project/html-to-json/',
        'CI': 'https://travis-ci.com/fhightower/html-to-json.svg?branch=main',
    },
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=requirements,
    license='MIT License',
    zip_safe=True,
    keywords='html to json,html,json,conversion',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
