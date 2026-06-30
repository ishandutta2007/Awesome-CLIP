# ViT-Backed CLIP (Transformer Dominant)

## Overview
Uses a Vision Transformer (ViT) as the visual backbone, dividing input images into patches and using self-attention to process global spatial relationships.

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
graph LR
    Image[Image] --> Patches[Patch Extraction]
    Patches --> LinearProj[Linear Projection & Position Embeddings]
    LinearProj --> ViT[ViT Transformer Blocks]
    ViT --> Output[Global Visual Representation]
```

## First Used
- **Year:** 2021
- **Paper:** [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)

[Back to Awesome-CLIP README](../README.md)
