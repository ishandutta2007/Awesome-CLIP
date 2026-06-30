# Multilingual CLIP (mCLIP)

## Overview
Multilingual CLIP replaces or aligns the text encoder with multi-lingual transformers, expanding zero-shot capabilities to dozens of languages.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph TD
    MultilingualText[Multilingual Text Input] --> MEncoder[Multilingual Text Encoder (e.g. XLM-R)]
    Image[Image] --> VEncoder[Visual Encoder]
    MEncoder --> CrossModal[Cross-Modal Alignment]
    VEncoder --> CrossModal
```

## First Used
- **Year:** 2022
- **Paper:** [Cross-lingual and Multilingual CLIP](https://aclanthology.org/2022.lrec-1.742/)

[Back to Awesome-CLIP README](../README.md)
