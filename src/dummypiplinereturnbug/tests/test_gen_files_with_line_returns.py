from __future__ import print_function, with_statement

import sys
import os
import itertools
import hashlib

import shutil

## Aux functions
def fullpath(relpath):
    '''Relative path to absolute'''
    if (type(relpath) is object or hasattr(relpath, 'read')): # relpath is either an object or file-like, try to get its name
        relpath = relpath.name
    return os.path.abspath(os.path.expanduser(relpath))

def path_sample_files(type=None, path=None, createdir=False):
    """ Helper function to return the full path to the test files """
    subdir = ''
    if not type:
        return ''
    elif type == 'input':
        subdir = 'files'
    elif type == 'results':
        subdir = 'results'
    elif type == 'output':
        subdir = 'out'

    dirpath = ''
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    if path:
        dirpath = fullpath(os.path.join(scriptpath, subdir, path))
    else:
        dirpath = fullpath(os.path.join(scriptpath, subdir))

    if createdir:
        create_dir_if_not_exist(dirpath)

    return dirpath

def create_dir_if_not_exist(path):
    """Create a directory if it does not already exist, else nothing is done and no error is return"""
    if not os.path.exists(path):
        os.makedirs(path)

def eq_textfiles(path1, path2):
    """ Comparison for text files, do a partial comparison, line by line, we compare only using "line2 in line1", where line2 is from file_partial """
    flag = True
    with open(path1, 'rt', newline='', encoding='utf-8') as f1, open(path2, 'rt', newline='', encoding='utf-8') as f2:
        flag = (f1.read() == f2.read())
    return flag

def eq_binfiles(path1, path2, blocksize=65535, startpos1=0, startpos2=0):
    """ Comparison for binary files, return True if both files are identical, False otherwise """
    flag = True
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        flag = (f1.read() == f2.read())
    return flag

## Pre-tests setup
def setup_module():
    """ Initialize the tests by emptying the out directory """
    outfolder = path_sample_files('output')
    shutil.rmtree(outfolder, ignore_errors=True)
    create_dir_if_not_exist(outfolder)

## Tests
def test_text_file():
    """ create a text file with unix line returns, then compare it with the same file pregenerated before """
    # Get paths
    fileout = path_sample_files('output', 'text_file.txt')  # file we will generate here
    filepregen = path_sample_files('results', 'pregen_text_file.txt')  # same file already generated before and saved in results (and hence unpacked by pip install -e git+...)
    # Write in the output file (text mode)
    with open(fileout, 'wt', newline='', encoding='utf-8') as f:
        f.write("First line\nSecond line\n\nThird line")
    # Compare the output file we just made, and the same file but pregenerated before
    assert eq_textfiles(fileout, filepregen)

def test_binary_file():
    """ same test for binary """
    # Get paths
    fileout = path_sample_files('output', 'binary_file.bin')  # file we will generate
    filepregen = path_sample_files('results', 'pregen_binary_file.bin')  # pregenerated file
    # Write in the output file (binary mode)
    with open(fileout, 'wb') as f:
        f.write(bytes("First line\nSecond line\n\nThird line", encoding='utf-8'))
    # Compare both files
    assert eq_binfiles(fileout, filepregen)
