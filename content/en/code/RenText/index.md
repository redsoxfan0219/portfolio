---
title: "RenText"
description: ""
lead: ""
date: 2022-06-22T22:31:50-04:00
lastmod: 2022-06-22T22:31:50-04:00
draft: false
images: []
menu:
  docs:
    parent: ""
weight: 30
toc: true
---

RenText is my ongoing effort to use computational tools to study Renaissance English texts, published roughly from 1470-1700. 

## Data Overview

The data used in this project is from the [Text Creation Partnership](https://textcreationpartnership.org/tcp-texts/eebo-tcp-early-english-books-online/).

The primary data currently consists of approximately 60,000 XML files, which can be accessed on the TCP's [Dropbox](https://www.dropbox.com/sh/pfx619wnjdck2lj/AAAeQjd_dv29oPymNoKJWfEYa?dl=0).

As described on [this page](https://textcreationpartnership.org/tcp-texts/eebo-tcp-early-english-books-online/), all of the 60K+ texts were hand-coded over the course of about 20 years. The exact nature of the [EEBO source texts](https://proquest.libguides.com/eebopqp)— digitized (often quite old and occasionally poor-quality)microfilm of original hard copies—makes [optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) infeasible.

### Data Updates

The latest updates from the TCP, available under "Phase II" on [this page](https://textcreationpartnership.org/tcp-texts/eebo-tcp-early-english-books-online/), indicate several thousand additional TCP texts are forthcoming. The page indicates this release was intended in 2020. However, as of October 2022, these updates have not been released.

## Tools

I'm using Python for all my exploratory data analysis and cleaning. My primary libraries are `pandas`, `re`, `xml.etree.ElementTree`, and `os`.

For visualization, I am using [graph modeling](https://cambridge-intelligence.com/graph-data-modeling-101/) with [neo4j](https://neo4j.com/).

## Completed Work

Thus far, I have 

- Written a script that converts all `.xml` files to clean, human-readable `.txt` files
- Uploaded all `.xml` files to [Amazon S3](https://aws.amazon.com/s3/), enabling cloud-based computing
- Cleaned errors and anomalies in the titles' publication dates, creating a [cleaned dates file](https://raw.githubusercontent.com/redsoxfan0219/RenText/main/cleaned_tcp_nav.csv) that can be used for as a look-up table
- Written a script that returns basic metadata (author, title) for all titles for a given year
- Written a script that returns a random book's information, including author, title, publication date, and sample paragraphs/lines of poetry
- Written a script to build a SQLite database with all primary metadata for all books in the TCP archive

## Plans

As of October 2022, my next steps include the following:

- Building an API to expose values in SQLite database
- Building a website to publish API calls to the SQLite database
- Building a Python package to simplify processing and analyze of TCP archive
- Building a graph database for visualizing the archive's metadata

## Codebase and Supporting Resources

The code for this project can be found on this [GitHub repository](https://github.com/redsoxfan0219/RenText).
