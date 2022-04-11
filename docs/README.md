---
layout: default
title: Workshop Overview
nav_order: 2
---

# Introduction to `conda`

This is the repository associated to the PICScIE Spring Workshop 2022 
'Introduction to Conda'.

The repo is divided into two sections `docs/`, which are the notes on various 
conda related topics, and `python-package`, which is a mini bare-bone python
package that is used as an example for creating your own conda package.

## Workshop's goals are

Providing you with the tools to make your software reproducible and impart 
some knowledge to you on how to publish your software using conda

* Understanding what
    * a package is
    * a package manager is
    * motivates the use of a package manager
* Some environment knowledge
    * How to create an environment 
    * How to work with files describing an environment (`environment.yml`)
    * Reproduce an environment
* Some package knowledge
    * How to install packages
    * How to create your own package
    * How to publish your own package

## What are ***not*** the goals of this workshop?

* Make you a Python wizard
* Teach you how to make a Python Package, even though we are doing it
* Completely `conda`-ify all of your software - that would be post workshop work

## Outline

1. [What is `conda`](docs/what-is-conda.md)
2. [Working with environments](docs/environments.md)
3. [Installing packages](docs/installing-packages.md)
4. [Creating packages](docs/creating-a-conda-package.md)
5. [Advanced Things](docs/)

## Requirements

The main requirement for this course is that you have some notion of how to work
with the (Linux) command line, and have a working Anaconda installation.

### Useful links

***Command line***:
* Be a command line wizard: [Intro to the Command Line](https://github.com/gabeclass/introcmdline)

***Anaconda***
* Install Anaconda: [Link](https://docs.anaconda.com/anaconda/install/index.html)

or less storage
* Install miniconda: [Link](https://docs.conda.io/en/latest/miniconda.html)

***`conda-build` Documentation for creating `conda` packages***:
* https://docs.conda.io/projects/conda-build/en/latest/index.html

***`conda` Cheatsheet***
* [Link](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

***Shameless plug***:
* How to make a python package: [Link](https://lsawade.github.io/how_to_make_a_python_package/index.html)


