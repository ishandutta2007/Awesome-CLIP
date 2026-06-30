# SigLIP (Sigmoid Pairwise Learning)

## Overview
In contrast to global normalization, SigLIP trains on pairwise binary logistic classification, solving scaling bottleneck and performance issues under limited VRAM.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph TD
    Img[Image Embeddings] --> Dot[Pairwise Dot Product]
    Txt[Text Embeddings] --> Dot
    Dot --> Logits[Logits Grid]
    Logits --> Sigmoid[Sigmoid Binary Loss]
```

## First Used
- **Year:** 2023
- **Paper:** [Sigmoid Loss for Language-Image Pre-training](https://arxiv.org/abs/2303.15343)

[Back to Awesome-CLIP README](../README.md)
