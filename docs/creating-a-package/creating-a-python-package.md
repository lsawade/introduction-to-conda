---
layout: default
title: Creating a Python Package
parent: Creating a Package 
nav_order: 1
---

# Creating a Python Package Pypi-style

As a part of the workshop we will learn how to create an `anaconda` package. For
that, we need to understand the structure needed to build a `python` package.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Structure of a mini Python package

```
1    intro2conda
2    |____environment.yml
3    |____README.md
4    |____setup.py
5    |____setup.cfg
6    |____src
7         |____intro2conda
8              |______init__.py
9              |____print.py
```

***Line-by-line***:

1. Main directory.
2. File that helps build a conda environment for the package.
3. Description of the package.
4. Installation script.
5. Installation configuration file that the installation script 
   looks for.
6. source code directory
7. package directory
8. file telling python that `intro2conda/` is a module
9. single module

## Installation

Change the directory to 
```bash
cd intro2conda
# or
cd /path/to/introduction-to-conda/intro2conda
and either 
```bash
python setup.py install [--editable]
```
or 
```bash
pip install [-e] .
```

### EDITABLE MODE!

`--editable` or `-e` allows us to edit the software after installation. Combined
with the 
```python
%load_ext autoreload
%autoreload 2
```
at the start of an `ipython` command line or jupyter noteboook session makes
debugging and developing a breeze. Whenever the code is edited `ipython` will
now re-import the function or module that as been editing to update the changes.



## Next: [Creating a `conda` package](creating-a-conda-package.md)