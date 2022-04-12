---
layout: default
title: Installing Packages
nav_order: 5
---

# Installing Packages

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

***Note***: It is worth noting here again that the packages that can be
installed do not have to be `python` packages. `conda` is language-agnostic and
will you can even create an environment without `python`. Nevertheless, `conda`
is mostly used to manage `python` environments at this point.

## Installing packages

The simplest way of install installing a package in the activate environment is
simply
```bash
conda install <PACKAGE>
```
and to update 
```bash
conda update <PACKAGE>
```

If you want to specify a different environment you can add the `--name` option 
```bash
conda install --name test-env <PACKAGE>
```

## Channel specification

Quite many packages come from specific channels. Most notably `pytorch`.
Channels can be specified using the `-c` option. 

***PyTorch***:
```bash
conda install -c pytroch pytorch
```

***NVIDIA Rapids for Power9 Architecture (Traverse)***
```bash
CHNL=https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda
conda create --name rapids-env --channel $CHNL cudf cuml
```

## Installing packages using Pip

`conda` will also track installations performed through `pip`. I.e. if you, for 
example installed `scipy` using `pip`
```bash
pip install scipy
```
`conda` is aware of this installation. You can even export the environment and
include the pip dependencies:
```bash
conda env export
```
***DISCLAIMER***: `conda env export --from history` does not include the `pip`
dependencies. There is an open issue for `conda` on GitHub to include this in 
future releases ([Github Issue](https://github.com/conda/conda/issues/9628)).


## Version constraints

Often, the package version has to be constraint by some range in version etc.
The table below shows an overview on how to apply the version constraints

| Constraint               | Specification            | Result               |
| ------------------------ | ------------------------ | -------------------- |
| Fuzzy                    | `numpy=1.11`             | 1.11.0, 1.11.1, etc. |
| Exact                    | `numpy==1.11`            | 1.11.0               |
| Greater than or equal to | `"numpy>=1.11"`          | 1.11.0 or higher     |
| OR                       | `"numpy=1.11.1\|1.11.3"` | 1.11.1 or 1.11.3     |
| AND                      | `"numpy>=1.8,<2"`        |                      |

***NOTE***: You have to use quotation marks if you are using any of [`> < | *`]
in the specification or if the specification contains a space.


## Next: [Creating a package](creating-a-package/index.md)