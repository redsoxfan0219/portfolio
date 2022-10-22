---
title: "Overview"
description: ""
lead: ""
date: 2022-10-21T22:16:14-04:00
lastmod: 2022-10-21T22:16:14-04:00
draft: false
images: []
menu:
  docs:
    parent: "Model Documentation"
weight: 20
toc: true
---

## Model Overview

### Model Purpose

The purpose of Super Fantastic Superior Sample Weather Model (hereafter "Sample Weather" or "the model") is to predict Fantastic Insurance Co.'s claim losses and loss frequencies following a catastrophic ("CAT") wind-rain event, such as a hurricane.

Currently, when a severe weather event occurs, Fantastic Insurance actuaries produce loss and frequency estimates by reviewing past wind-rain events and  applying a multiplication factor to the cost and frequencies of the previous event. This approach has proven ineffective at gauging losses and frequencies, especially when the present event differs dramatically in size and location from past wind-rain events.

The goal of the Sample Weather model is to use advanced analytics techniques to 

  - predict losses and frequencies more accurately
  - produce predictions more quickly than current practice allows, and
  - continue producing predictions for the 30 days following a wind-rain event.

### Model Characteristics

| Attribute | Value |
|-----------| ------|
|Model Name| Sample Weather Model|
|Model ID No.| 867-5309|
|Model Owner| Tommy Tutone|
|Model Client| Jenny Jenny|
|Production Date| November 16, 1981|
|Deployment SageMaker Image ID|325389189899.dkr.ecr.us-east-2.amazonaws.com/sampleenvironment-sampleweathermodel-dev-deploy:latest|

## Repository Details

**Production Repository**

[https://github.com/redsoxfan0219/master/sampleweathermodel]()

**Development Repository**

[https://github.com/redsoxfan0219/develop/sampleweathermodel]()

**ETL Code**

[https://github.com/redsoxfan0219/ETL/sampleweathermodel]()

**Final Training Data**

[s3://sample-environment/sampleweathermodel/eda/train/]()