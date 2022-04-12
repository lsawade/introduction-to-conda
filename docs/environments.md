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

Much like with anything out there it's always good to keep `conda` updated. This
is a good time to check whether your `conda` installation was successful to
begin with.
```bash
conda info
```
will show all the important info concerning your anaconda base environment or an
activated environment. If the command returns something along the lines of
`shell not properly set up to use conda` or `conda not found`, you can can
manually activate the base environment by calling
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
downloading the requested packages (unless they are cached), and will
subsequently install them. You can avoid the prompt by adding the `-y` option to
the creation command
```bash
conda create -y --name test-env "python>=3.9" matplotlib numpy
```
The final statement will show you the instructions on how to activate/deativate
the environment.
```bash
...
# To activate this environment, use
#
#     $ conda activate test-env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
Now you are ready to activate/enter the environment using:
```bash
conda activate test-env
```

To check whether the activation was successful, see whether the python version
you have in the environment is actually installed in your environment:
```bash
which python
```
If it does not return something like:
`path/to/anaconda/envs/test-env/bin/python`, then you are in trouble.


## Remove an environment

If your environment contains unreconcilable version conflicts, or you are simply
tired of your environment, you can remove it using
```bash
conda env remove --name test-env
```

## Showing the environments contents

To show a list of the packages that are installed in the environment use
```bash
conda list 
```

For the exact URL of every installable `conda` package use the `--explicit`
option
```bash
conda list --explicit
```

We can even export the output to a file and recreate the environment using the
source URLs only
```bash
conda list --explicit > test-env-explicit.yml
```
and 
```bash
conda create --name test-env-2 --file test-env-explicit.yml
```
***Note***: This only works if you are on (at least) the same platform. Most of
the associated links in `test-env.yml` will point to platform specific
`channels`, so if you create the file on `macOS` it will not work on `Darwin`

## Create an `environment.yml`

In the above example, we actually already created an `environment.yml`. So,
why is there another section? 

As mentioned above the `explicit` form of an `environment.yml` is platform
dependent. We can't however assume that everyone is working on the same
platform. Most of us don't. Almost everyone here has either a Mac or a Windows
machine, but the campus clusters all run Linux. A work around is a platform
independent `environment.yml` that can be used to recreate the environment on
any machine.

***NOTE***: I have written `.yml` quite a lot now. Discussion the actual format
is beyond the scope of this workshop, but I will leave you with a link to the
[YAML Documentation](https://yaml.org).

### From scratch

A conda `environment.yml` has some necessary content (unless it's the explicit
type from the previous section).
```yaml
name: test-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python>=3.9
  - matplotlib
  - numpy
```
`name` is the name of the enviroment. `channels` tell `conda` where to look for
packages online. For example, `pytorch` requires a specific channel: `channel:
pytorch`. `dependencies` are the packages that we have installed manually
earlier. It is important to note here that we have not provided any version
information for the two python packages. This is ok in most cases, `conda` will
simply look for the most recent, non-conflicting versions of the packages. In
case, you are planning on publishing a code using a certain environment, make
sure that you do provide version numbers for reproducibility. A full guide on
how to define version numbers is given at the end of the
[Cheatsheet](cheatsheet.md).

Let's use this file to create the enviroment
```bash
conda env create -f test-env.yml
```
If the enviroment still exists remove it or give it a different name by using
the `--name <env-name>` option. Since we are using a file we will not be
prompted whether we want to create the environment.


## Export an environment & reproduce it

Feeling lazy one can actually export all the information needed to recreate the 
enviroment:
```bash
conda env export
```
This will return an `enviroment.yml` with the exact version and the "hash"-code.
This is often too much information and makes it incredible hard to transfer the
environment to other machines. Therefore a better option is to just export the
packages we installed by hand
```bash
conda env export --from-history 
```
which should return:
```yaml
name: test-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python[version='>=3.9']
  - matplotlib
  - numpy
prefix: <path-to-anaconda>/envs/test-env
```
If you want to save this to a file simple add the `-f` option:
```bash
conda env export --from-history -f test-env.yml
```
Finally, we can use this `environment.yml` to recreate the environment with as
much or as little version information as you want.
```bash
conda create env -f test-env.yml
```

Now that we know all about creating and recreating environments, we can start
by installing packages.


## Next: [Installing Packages](installing-packages.md)