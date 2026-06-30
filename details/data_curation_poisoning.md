# The Data Curation and Poisoning Bottleneck

## Overview
Mitigating dataset issues such as alt-text noise and adversarial split-view/frontrunning data poisoning using data filtering pipelines (e.g. LAION aesthetic filters) or robust training objectives.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph TD
    RawData[Raw Web Scraped Data] --> DataFiltering[Data Filtering Pipeline (Aesthetic / Text Quality)]
    DataFiltering --> CleanData[Clean Image-Text Pairs]
    CleanData --> RobustTraining[Contrastive Pre-training]
```

## First Used
- **Year:** 2023
- **Paper:** [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149)

[Back to Awesome-CLIP README](../README.md)
