#!/usr/bin/env python
# coding=utf-8

import sys
import os

CURRENT_PATH = os.getcwd()
BASE_PATH = CURRENT_PATH
PYTHON_VERSION = sys.version_info.major
input = raw_input if PYTHON_VERSION == 2 else input

joinpath = lambda p, name: os.path.join(p, name)

def cin(prompt='', default_input=''):
    tmp = input(prompt)
    # tmp = tmp.strip()
    return default_input if not tmp else tmp

def delete(p, filename):
    if os.path.exists(joinpath(p, filename)):
        os.remove(joinpath(p, filename))


def make():

    # tips:
    print('##########################################')
    print('#    Welcome to use Makesetup Program    #')
    print('##########################################')

    delete_old = cin('Would you like to delete old setup files ? (y|N)')
    if delete_old.lower() not in ('y', 'Y', 'yes', 'Yes', 'YES'):
        print('\n  You have rejected to delete old setup file.')
        print('So cancel this program.\n')
        sys.exit(-1)

    # 1
    proj_path = cin('\nProject Path: ', CURRENT_PATH)
    proj_name = cin('Project Name: ', None)
    proj_dir = cin('Project Dir: ', None)
    version = cin('Version: ', '0.0.1')
    description = cin('Description: ')
    author = cin('Author: ')
    author_email = cin('Author Email: ')
    requires = cin('Requires (separate with ","): ').split(',')

    home_page = cin('Home Page: ')
    license = cin('License: ', 'Apache 2.0')
    # summary = cin('Summary: ')
    # keywords = cin('Keywords: ')
    # platform = cin('Platform: ', 'Linux/Unix')
    # download_url = cin('Download URL: ')
    # provider = cin('Provider: ')
    # classifiers = input('Classifiers: ')
    classifiers = (
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        )
    # zip_safe = False

    ## delete old files
    delete(proj_path, 'setup.py')
    delete(proj_path, 'README.rst')
    delete(proj_path, 'HISTORY.rst')
    delete(proj_path, 'README.md')
    ##

    with open(joinpath(proj_path, 'README.rst'), 'w') as fp:
        fp.write('Project: %s \n -----------------------\n' % proj_name)

    with open(joinpath(proj_path, 'HISTORY.rst'), 'w') as fp:
        fp.write('Project History: %s \n -----------------------\n' % proj_name)

    with open(joinpath(proj_path, 'setup.py'), 'w') as fp:
        # base
        fp.write('''
#!/usr/bin/env python 
# coding=utf-8
        
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.rst', 'r') as fp:
        readme = fp.read()
except :
    readme = ''
try:
    with open('README.md', 'r') as fp:
        readme = fp.read()
except :
    pass

try:
    with open('HISTORY.rst', 'r') as fp:
        history = fp.read()
except :
    history = ''
        ''')

        fp.write('\n\nsetup(\n')
        # Package Info Begin

        fp.write('\tname = %s\n' % proj_name)
        fp.write('\tversion = %s\n' % version)
        fp.write('\tdescription = %s\n' % description)
        fp.write('\tlong_description = readme + history\n')
        fp.write('\tauthor = %s\n' % author)
        fp.write('\tauthor_eamil = %s\n' % author_email)
        fp.write('\turl = %s\n' % home_page)
        fp.write('\tpackages = %s\n' % proj_name.split(','))
        fp.write('\tpackage_dir = {"%s": "%s"}\n' % (proj_name, proj_dir))
        fp.write('\tinclude_package_data = True\n')
        fp.write('\tinstall_requires = %s\n' % requires)
        fp.write('\tlicense = "%s"' % license)
        fp.write('\tzip_safe = False\n')
        fp.write('\tclassifiers = %s' % str(classifiers))
        fp.write('\tentry_points = {"console_scripts": ["%s = %s.__main__:main"]}' % (proj_name, proj_name))

        # Package Info End
        fp.write('\n)\n')

if __name__ == '__main__':
    make()