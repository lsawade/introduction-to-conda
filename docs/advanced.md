---
layout: default
title: Cheatsheet
nav_order: 7
---

# Some advanced things

## Environment Variables

You can define environment variables in conda configuration file, so that
whenever your environment is loaded you have environment variables are set. This
works well for configuration parameters but lacks in versatility for path
descriptions.

An example for setting a configuration parameter. ***Disclaimer*** don't use
this if your software has a lot of parameters to define, and these parameters
control all of the software. A file that is more easily written and changed that
is read as a config file upon running the software is probably a better choice
(eg. [TOML](https://toml.io/en/)).

```bash
echo $PSTYLE
```

```python
from intro2conda.print import customprint

pdict = dict(
    hello=dict(princeton=1, USA=2, world=3), 
    bye=dict(princeton=1, USA=2, world=3))
customprint(pdict)
```

Update `PSTYLE` and run again

```python
from intro2conda.print import customprint

# Make dictionary
pdict = dict(
    hello=dict(princeton=1, USA=2, world=3), 
    bye=dict(princeton=1, USA=2, world=3))

# Print dictionary 2 different ways depending on an environment variable
customprint(pdict)
```

### Why can't/shouldn't we use this with paths?

The `environment.yml` is not very dynamic in the sense that it is not aware of/cannot parse standard path descriptions such as `$HOME`, `$USER` etc. So, if you define a path it needs to be the exact path making it not very portable/reproducible. Unless you know that you are always going to be on a single machine in a single location. Then, setting the as an environment variable may be ok!



