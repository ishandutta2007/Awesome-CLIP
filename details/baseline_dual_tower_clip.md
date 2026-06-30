# The Baseline Dual-Tower Era (OpenAI CLIP, 2021)

## Overview
The foundational dual-tower architecture that pairs an Image Encoder (Vision Transformer or ResNet) with a Text Encoder (Transformer) in parallel. It computes similarity across image-text pairs using InfoNCE loss to align representations.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph TD
    Image[Raw Image] --> ImageEncoder[Image Encoder (ViT/ResNet)]
    Text[Raw Text] --> TextEncoder[Text Encoder (Transformer)]
    ImageEncoder --> ImageEmbed[Image Representation (h_i)]
    TextEncoder --> TextEmbed[Text Representation (h_t)]
    ImageEmbed --> Project[Projection Head]
    TextEmbed --> Project
    Project --> CosSim[Cosine Similarity Matrix]
    CosSim --> Loss[InfoNCE Loss]
```

## First Used
- **Year:** 2021
- **Paper:** [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)

[Back to Awesome-CLIP README](../README.md)
