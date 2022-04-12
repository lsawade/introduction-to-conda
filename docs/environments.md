---
layout: default
title: Environments
nav_order: 4
---

# Environments

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Update the base environment

Much like with anything out there it's always good to keep `conda` updated.
This is a good time to check whether your `conda` installation was successful 
to begin with.
```bash
conda info
```
will show all the important info concerning your anaconda base environment or an
activated environment. If the command returns something along the lines of 
`shell not properly set up to use conda` or `conda not found`, you can
can manually activate the base environment by calling
```bash
source ~/<path_to_anaconda>/etc/profile.d/conda.sh
```
This may ask you whether you want to append the `conda init` to your `.bashrc`,
which in most cases you want to answer with `Y(es)`. Try again to get the `conda
info`.  If everything's alright, you should be able update the base environment.
```bash
conda update conda
```
Once the base environment is updated, we can proceed with creating environments.

***PRINCETON HPC DISCLAIMER***: On the clusters you are not able to update the
base environment because you do not have the rights to modify the base
installation of conda. This is a good thing -- imagine one of your peers
fiddling around with the campus installation...

## Create an environment

To create a `conda` environment use the following line

```bash
conda create --name test-env
```

You may also add some extra terms to already start installing packages:

```bash
conda create --name test-env "python>=3.9" matplotlib numpy
```

`conda` will then proceed to check for the best possible versions of your
packages, then prompt you with the question whether you want to proceed or not
`[Y/N]`. Type `y` followed by `Return`, and `conda` will proceed with
downloading the needed 

## Remove an environment



## Create an `environment.yml`

## Export an environment

## Reproduce an environemt


