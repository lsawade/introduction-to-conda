---
layout: default
title: Overview
nav_order: 1
---

# Introduction to `conda`

This is the documentation associated with the PICScIE Workshop 
'Introduction to Conda' (Spring 2022).

The full documentation for the course is located here: 
[Documentation](https://lsawade.github.io/introduction-to-conda/)

The courses repo is located here
[Github Repo](https://github.com/lsawade/introduction-to-conda)


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


The repo is divided into two sections `docs/`, which are the notes on various
`conda` related topics, and `intro2conda`, which is a miniscule python
package that is used as an example for creating your own `conda` package.

## Workshop goals

Providing you with the tools to make your software reproducible and impart 
some knowledge to you on how to publish your software using `conda`

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

## ***Not*** workshop goals

* Make you a Python wizard
* Teach you how to make a Python Package, even though we are doing it
* Completely `conda`-ify all of your software - that would be post-workshop work

## Requirements

The main requirement for this course is that you have some notion of how to work
with the (Linux) command line, and have a working Anaconda installation.

## Getting Started

You technically don't need anything to get started, but I created a repo with
all the docs and a tiny Python package that we will use to create and upload our
first `conda` package. So let's just clone it for now and then we will get
started.

```bash
git clone git@github.com:lsawade/introduction-to-conda.git
```
Then,
```bash
cd introduction-to-conda
```

## Course Outline

1. [What is `conda`?](what-is-conda.md)
2. [Environments](environments.md)
3. [Installing Packages](installing-packages.md)
4. [Creating packages](creating-a-package/index.md)
    1. [Creating a Python package](creating-a-package/creating-a-python-package.md)
    2. [Creating a Conda package](creating-a-package/creating-a-conda-package.md)
5. [What is `mamba`?](mamba.md)
6. [Advanced examples](advanced.md)
7. [Cheatsheet](cheatsheet.md)

---

## Useful links

***Command line***:
* Be a command line wizard: [Intro to the Command Line](https://github.com/gabeclass/introcmdline)

***Anaconda Installation***
* Install Anaconda: [Link](https://docs.anaconda.com/anaconda/install/index.html)

or less storage
* Install miniconda: [Link](https://docs.conda.io/en/latest/miniconda.html)

***Documentation for `conda-build` and creating `conda` packages***:
* [Link](https://docs.conda.io/projects/conda-build/en/latest/index.html)

***YAML Documentation***
* [Link](https://yaml.org)

***Cheatsheet for `conda`***
* [Link](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

***Shameless plug***:
* How to make a python package: [Link](https://lsawade.github.io/how_to_make_a_python_package/index.html)
