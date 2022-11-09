---
title: "Model Documentation"
description: "A sample of AI/ML Model Documentation"
lead: ""
date: 2022-06-22T20:02:18-04:00
lastmod: 2022-06-22T20:02:18-04:00
draft: false
images: []
menu:
  docs:
    parent: "sample-work-products"
weight: 40
toc: true
---

Below is an example of AI-ML documentation that I've created in the past. The content of this text is designed to meet expectations established in the [Federal Reserve's SR 11-7: Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm).

**Note on style:** The text below relies heavily on passive voice. This is by design. Model documentation style guides recommend erring on the side of passive voice when the agent is not important or the agent is a computer script or automation process. I also do not use the second-person present tense here because this is not an instructional manual. For an example of text that more closely follows commonly used style guides (e.g., [Google's developer documentation style guide](https://developers.google.com/style)), see my [Introduction to the Command Line for Technical Writers](https://benbarksdale.netlify.app/docs/guides/introduction-to-the-command-line-for-technical-writers/).

**Disclaimer: all proprietary details have been removed and the specific model attributes outlined below have been invented.**

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

## Model Outputs

The model produces state-level loss and frequency estimates for the lower 48 states + the District of Columbia. The production code sends 98 model outputs to Teradata and the business partner's S3 bucket. The output format is `.csv`.

## Implementation Details

The model pipeline is triggered to run when a member of the catastrophe claims team registers a new catastrophic event ID within their Super Great Claims system. New IDs are typically established while storms are still forming off the Atlantic coast (i.e., before any related claims are filed).

When new claims are filed following a catastrophic event, the model runs each of the first 30 days after claim with the new CAT ID is filed. The model runs at 8:00 ET on the applicable days. The business SLA states that the model must upload predictions to the business S3 by 9:00 am ET on the applicable days.

## Production Data

### Data Input #1: New Claim Data

The first production data input consists of variables related to each of the new claims filed. Only claims that have the specific CAT ID flag are passed to the model. The following are the raw claim variables passed to the model:

| Variable | Definition | Units |
|----------|------------|-------|
| `claim_id` | 16-digit Unique identifier | N/A |
| `req_dol` | Total amount filed amount in claim | USD |
| `cocode` | US county code of claim location | N/A |
| `loss_desc` | Text description of the loss | N/A |
| `written` | Total written premium of the policy | USD |

### Data Input #2: Claimant History

The second data input includes the policyholder's claim history.

| Variable | Definition | Units |
|----------|------------|-------|
| `claim_id` | 16-digit Unique identifier | N/A |
| `pr_cl_fd` | Binary flag indicating prior claim filed on the policy in the last 12 months | N/A |
| `pr_frd_nt` | Binary flag indicating prior fraud investigation of policyholder | N/A |
|`inv_notes` | String of prior fraud investigator notes, if applicable; different incidents' notes separated by semicolon | NA |

#### Rationale

Claim history is used to predict potential incidents of fraud. Historically, catastrophic events have invited high levels of insurance fraud.

#### Cleaning, Transformations, and Feature Engineering

Claimant history is filtered to limit to the prior 6 months before the first filed CAT claim.

The fraud investigator notes are stemmed and lemmatized before undergoing TF-IDF counting. The static file (`.csv`)outlining the most important n-grams are sourced from the production S3 bucket.

### Data Input #3: NOAA Weather Data

Weather data is sourced from the National Oceanic & Atmospheric Administration's [High-Resolution Rapid Refresh](https://rapidrefresh.noaa.gov/hrrr/) system. 

### Data Input #4: Prior Day Model Objects

Past Model Objects.

## Methodology, Assumptions, and Parameters

The primary modeling framework is XGBoost, whose objective function is the sum of a training loss and a regularization metric. For more information on the model equation, see [here](https://xgboost.readthedocs.io/en/stable/tutorials/model.html).

For each of this project's model objects, the modeling team tuned the following hyperparameters:

- `alpha` (range: 0-1000)
- `colsample_bytree` (range: .1-.5)
- `eta` (learning rate)(range: .1-.5)
- `lambda`(range: 0-1000)

The hyperparamters values vary for each of the 30 n-day models. The list of values can be found in the `xgb_hp_values.csv` file, available in the project S3 bucket.

## Controls

### Input Controls

The following are the input controls for the production model:

- Incoming variables from each source are tested against dictionaries of expected variables. If there are meaningful discrepancies, the model execution fails and an error message is logged on AWS CloudWatch.

### Output Controls

For each model run, the following output controls are performed:

- A log of each model run is saved to the production S3 bucket
- When the model outputs land in the business partner S3, a confirmation email is sent to the business partner and the lead modeler. 
