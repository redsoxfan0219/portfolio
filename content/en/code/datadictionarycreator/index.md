---
title: "Data Dictionary Creator"
description: ""
lead: ""
date: 2022-06-22T22:31:36-04:00
lastmod: 2022-06-22T22:31:36-04:00
draft: false
images: []
menu:
  docs:
    parent: ""
weight: 10
toc: true
---

My first Python package, `adamic`, is a simple solution for creating data dictionaries. 

## Installation

The package is available on [PyPi](https://pypi.org/project/adamic/) and can be downloaded by running the following from the command line:

```sh
pip install adamic
```

## Use

After installing the package to your environment, import the package to your script, Jupyter notebook, or directly to the `python3` command line.

```python
from adamic import adamic
```

To create your data dictionary, pass a Pandas dataframe to the `create_data_dictionary()` function:

```python
adamic.create_data_dictionary(sample_df)
```

The package will prompt you to supply definitions for each variable in the dataset. Hit `Enter` after supplying definition or if you want to define the variable later after the output file has been created.

Finally, you will be prompted to name your preferred file extension. `.csv`, `.json`, and `.xlsx` are the available options.

## Source Code

The source code for `adamic` can be found at [this GitHub repository](https://github.com/redsoxfan0219/adamic).