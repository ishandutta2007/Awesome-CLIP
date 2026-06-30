# Cross-Modal Projection Heads

## Overview
Small linear or MLP projection layers that map unimodal visual and text encoder states into a joint embedding space for contrastive training.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph TD
    VHidden[Vision Encoder Output] --> VProj[Vision MLP Projection Head]
    THidden[Text Encoder Output] --> TProj[Text MLP Projection Head]
    VProj --> Shared[Shared Semantic Space (e.g. 512-dim)]
    TProj --> Shared
```

## First Used
- **Year:** 2020
- **Paper:** [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)

[Back to Awesome-CLIP README](../README.md)
