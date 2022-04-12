---
layout: default
title: Advanced
nav_order: 7
---

# Some advanced things

## Environment Variables

You can define environment variables in `enviroment.yml` file, so that
whenever your environment is loaded you have environment variables are set. This
works well for configuration parameters but lacks in versatility for path
descriptions.

***Disclaimer***: Don't use this if your software has a lot of parameters to
define, and these parameters control all of the software (say simluations). A
file that is more easily written and changed that is read as a config file upon
running the software is probably a better choice (eg.
[TOML](https://toml.io/en/), or [YAML](https://yaml.org)).

### Set environment variables in the `environment.yml`

***An example for setting a configuration parameter***:

If we used an `environment.yml` with the following content:

```bash
channels:
  - conda-forge
  - defaults
dependencies:
  - python>=3.8
  - pip:
    - -e .
variables:
  PSTYLE: PRETTY
```
and created the enviroment, the variable `PSTYLE` is set upon activation. We
can check using:
```bash
echo $PSTYLE
```
or
```bash
conda env config vars list
```

Then, for example, in `python` we can print depending on the environment
variable set in the `environment.yml`.


```python
from intro2conda.print import customprint

pdict = dict(
    hello=dict(princeton=1, USA=2, world=3), 
    bye=dict(princeton=1, USA=2, world=3))
customprint(pdict)
```

Exit python, update `PSTYLE` to a different value than `PRETTY`,
and run again to see the change.

### Setting enviroment variables after creating the environment

We can set environment specific variables after we already created the
environment using the following syntax
```bash
conda env config vars set my_var=value
```
For the environment, this change is permanent, meaning that after deactivation,
and reactivation the variable will be available again!

It will also be included now, when exporting the environment:
```bash
conda env export --from-history 
```

### Why can't/shouldn't we use this with paths?

The `environment.yml` is not very dynamic in the sense that it is not aware
of/cannot parse standard path descriptions such as `$HOME`, `$USER` etc. So, if
you define a path it needs to be the exact path making it not very
portable/reproducible. Unless you know that you are always going to be on a
single machine in a single location. Then, setting the as an environment
variable may be ok!


## Github workflows

A lot of things can be automated using github workflows. Github workflows are
`.yml` files that are in the `.github/` directory in your repository. In only a
few step you can, e.g., set up unit testing, so that your package is tested with
every `push`, or `pull request`. The files are rather lengthy and beyond the 
scope of the workshop but I wanted to mention them here because Github workflows 
can be used for building and uploading your conda package so that you do not 
have to do that.

