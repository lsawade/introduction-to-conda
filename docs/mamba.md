---
layout: default
title: Mamba
nav_order: 7
---
# `mamba`?

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>



## What is `mamba`?

[`mamba`](https://mamba.readthedocs.io/en/latest/index.html) is much like
`conda` a package manager and supports most of the features that `conda`
does, such as conflict management, environment creation, etc.

In most cases you can just replace the `conda` command with `mamba` and you
should still be fine with installing packages, and creating environments.

## Why `mamba`?

So, why am I bringing this up if they're all the same? Well, `mamba` is written
entirely in `C++` making it a lot faster than `conda`. In fact, having used 
`conda` for a while, it's main disadvantage is speed, in particular when 
environments become very large.

One of the coolest feature is
[`repoquery`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery)

Repoquery can easily and efficiently show you dependency structure of the
package you want to install.

## Why not `mambda`?

AlthoughMamba has been growing quite rapidly, it’s just not yet as widely
spread. Hence, bugs and oter kinks haven't been fully ironed out yet. This may
change though. As of now, the main disadvantage is that mamba’s incompatibility
detection is not as “good” as conda’s (yet). So, if you want your research to be
reproducible, I suggest to stick with `conda` for now, but keep an eye on
`mamba`.


## Next: [Advanced Examples](advanced.md)

