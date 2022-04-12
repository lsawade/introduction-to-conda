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

## Conda skeleton