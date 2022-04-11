# Creating a Python Pacakge Pypi-style

As a part of the workshop we will learn how to create an anconda package. For that, 
we need to understand the parebone needs for a pyhton package.

## Structure of a very barebon Python package

```directory
1    python-package
2    |____environment.yml
3    |____README.md
4    |____setup.py
5    |____setup.cfg
6    |____src
7    |    |____intro2conda
8    |    |    |______init__.py
9    |    |    |____print.py
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

Either 

```bash
python setup.py install [--editable]
```

or 

```bash
pip install [-e] .
```

`--editable` or `-e` allows us to edit the software after installation. Combined with the 

```python
%load_ext autoreload
%autoreload 2
```

at the beginning of an `ipython` command line or jupyter noteboook makes debugging and developing a breeze. Whenever the code is edited `ipython` will now re-import the function or module that as been editing to update the changes.