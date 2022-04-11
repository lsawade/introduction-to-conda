# Cheat sheet

There is an official cheatsheet (see
[here](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)),
but I decided to highlight some commands, that I definitely use on a close to 
daily basis.

## Basics

| Command                     | Description                                  |
| --------------------------- | -------------------------------------------- |
| `conda info`                | Verify `conda` is installed, and its version |
| `conda update conda`        | Update `conda`                               |
| `conda install PACKAGENAME` | Install package                              |
| `conda update PACKAGENAME`  | Update specific package                      |
| `COMMANDNAME --help`        | Command line help                            |


## Environemts

| Command                                                    | Description                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------- |
| `conda create --name py35 python=3.5`                      | Create a new environemt name py35, install Python 3.5                     |
| `conda activate ENVIRONMENT`                               | Activate the specficic environment                                        |
| `conda env list`                                           | List all environment                                                      |
| `conda create --clone py35 --name py35-2`                  | Create clone of the original environment (DONT JUST COPY!!!)              |
| `conda list`                                               | List all Packages instsalled in the environment                           |
| `conda list --explicit > hello-env.txt`                    | Save environment to text file                                             |
| `conda env remove --name hello-env`                        | Remove environment with the name hello-env                                |
| `conda deactivate`                                         | deactivate environment                                                    |
| `conda env create [--name hello-env] --file hello-env.yml` | Create new environment from file with optional name                       |
| `conda create --name hello-env hellopython`                | Stacking commands: create new env, name it hello-env, install hellopython |


## Finding and installing packages

| Command                                       | Description                                                    |
| --------------------------------------------- | -------------------------------------------------------------- |
| `conda search PACKAGENAME`                    | Search for a specific package                                  |
| `conda install jupyter`                       | Install package, here jupyter, in active env                   |
| `conda install --name hello-env toolz`        | Install package in a specific environment                      |
| `conda install --channel conda-forge boltons` | Install package (boltons) from a specfic channel (conda-forge) |
| `pip install boltons`                         | Install package (boltons) directly from Pypi in current env    |
| `conda remove --name hello-env toolz boltons` | Remove one or more packages from (hello-env)                   |

## Managing multiple versions of Python

If you need 2 or more different versions of `python` the recipe is to create
multiple environments, so that the `python` versions do not interfere with each
other.

Check which python you are running:
```bash
# Windows
where python

# Linux/macOS
which -a python
```

Check the version of Python using `python --version`


## Define version numbers

| Constraint               | Specification          | Result               |
| ------------------------ | ---------------------- | -------------------- |
| Fuzzy                    | `numpy=1.11`           | 1.11.0, 1.11.1, etc. |
| Exact                    | `numpy==1.11`          | 1.11.0               |
| Greater than or equal to | `"numpy>=1.11"`          | 1.11.0 or higher     |
| OR                       | `"numpy=1.11.1\|1.11.3"` | 1.11.1 or 1.11.3     |
| AND                      | `"numpy>=1.8,<2"`        |                      |

***NOTE***: You have to use quotation marks if you are using any of [`> < | *`]
in the specification or if the specification contains a space.