---
layout: default
title: Creating a Conda Package
parent: Creating a Package 
nav_order: 2
---

# Creating a conda package

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Install/update the `conda-build` package

For the creation of `conda` packages you should always update the builder:
```bash
conda install conda-build
```
or
```bash
conda update conda
conda update conda-build
```

## Requirements

The requirement to build a `conda` package is a working `meta.yml` that contains
a build recipe. After successful building you will need an `anaconda.org` 
account to upload and distribute the package.

Let's start with the `meta.yml`

### `meta.yml`

The full documentation for the `meta.yml` is found
[here](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#run).
A small breakdown is listed below.

The `meta.yml` contains all the small things needed to updaload a `conda`
package:
* name
* version number
* software requirements on the machine running the builder and the future host
* test scripts and paths

The most important parts of the `meta.yml` are:

```yaml
...
package:
  name: "{{ name|lower }}"
  version: "{{ version }}"

source:
  path: ./

build:
  skip: true # [win]
  number: 0
  script: "{{ PYTHON }} -m pip install . --ignore-installed -vv "

requirements:
  host:
    - python >=3.8
    - pip
  run:
    - python >=3.8

test:
  imports:
    - intro2conda
    - intro2conda.print
...
```

The `package` description defines name and version number. `source` defines
where to get the package from relative to the path of the `meta.yml`. This could
also be a `git_url` or a `url` that grabs a `tar` ball. `build/script` does not
have to be a one-liner, but could also be a path to an actual build script
relative to the location of the `meta.yml` file. `requirements` asks for the
necessary software needed to run the build process and the necessary software
for potential hosts, e.g. `osx-64`. The software can be compilers that are
called with a specified `build.sh` (`macos`, `Linux`) or `bld.bat` (`windows`).
Finally, `test` could be specified as a script/command or in form of `python`
module names under `imports`.

### Building the conda package

The `meta.yml` is located in our main `intro2conda` dir. 
To run the build
process and output the packages locally please run:
```bash 
conda build intro2conda --croot pkgs
```
where the `--croot` option and its argument define the package output path.

### Indexing

If everything goes smoothly, we can index the packaged directory, so that conda
knows we have a package here. 
```bash
conda index pkgs
```
Should only take a fraction of a second

### Installing the local package

Finally we can install the local package using
```bash
conda install --use-local -c ./pkgs intro2conda
```

### Updoading the package

Make anaconda account on [anaconda.org](https://anaconda.org/) and enter the
credentials when being prompted. 

```bash
anaconda upload path/to/introduction-to-conda/pkgs/osx-64/intro2conda-0.0.1-py310_0.tar.bz2
```

If the download is successful you should be able to
```bash
conda install -c <username> intro2conda
```

***NOTE***: You can delete the `intro2conda` from your channel after uploading
on [anaconda.org](https://anaconda.org/)


## Next: [What's `mamba` now?](../mamba.md)