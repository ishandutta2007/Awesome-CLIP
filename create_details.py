import os

details_dir = r"C:\Users\ishan\Documents\Projects\Awesome-CLIP\details"
os.makedirs(details_dir, exist_ok=True)

topics = [
    {
        "filename": "baseline_dual_tower_clip.md",
        "title": "The Baseline Dual-Tower Era (OpenAI CLIP, 2021)",
        "year": "2021",
        "paper": "[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)",
        "description": "The foundational dual-tower architecture that pairs an Image Encoder (Vision Transformer or ResNet) with a Text Encoder (Transformer) in parallel. It computes similarity across image-text pairs using InfoNCE loss to align representations.",
        "mermaid": """graph TD
    Image[Raw Image] --> ImageEncoder[Image Encoder (ViT/ResNet)]
    Text[Raw Text] --> TextEncoder[Text Encoder (Transformer)]
    ImageEncoder --> ImageEmbed[Image Representation (h_i)]
    TextEncoder --> TextEmbed[Text Representation (h_t)]
    ImageEmbed --> Project[Projection Head]
    TextEmbed --> Project
    Project --> CosSim[Cosine Similarity Matrix]
    CosSim --> Loss[InfoNCE Loss]"""
    },
    {
        "filename": "sigmoid_loss_siglip.md",
        "title": "The Sigmoid Loss & Open Scaling Era (SigLIP, 2023)",
        "year": "2023",
        "paper": "[Sigmoid Loss for Language-Image Pre-training](https://arxiv.org/abs/2303.15343)",
        "description": "SigLIP replaces standard InfoNCE loss with a pairwise sigmoid loss. This decouples contrastive scaling from batch size, allowing training with much lower memory requirements and greater efficiency.",
        "mermaid": """graph TD
    ImageEmbed[Image Embeddings] --> Pairwise[Pairwise Matcher]
    TextEmbed[Text Embeddings] --> Pairwise
    Pairwise --> BinaryClass[Independent Binary Classification]
    BinaryClass --> SigmoidLoss[Sigmoid Loss]"""
    },
    {
        "filename": "unified_token_generative.md",
        "title": "The Unified Token & Generative Autoregressive Era (~2024–Present)",
        "year": "2024",
        "paper": "[Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818)",
        "description": "Modern multimodal models integrate visual tokenization directly into the LLM backbone rather than keeping separate text/vision towers, enabling unified interleaved token processing.",
        "mermaid": """graph LR
    Image[Image] --> Tokenizer[Visual Tokenizer]
    Text[Text] --> Tokenizer2[Text Tokenizer]
    Tokenizer --> Autoregressive[Unified Autoregressive Transformer]
    Tokenizer2 --> Autoregressive
    Autoregressive --> Output[Interleaved Multimodal Generation]"""
    },
    {
        "filename": "standard_clip_infonce.md",
        "title": "Standard CLIP (InfoNCE Dual-Tower)",
        "year": "2021",
        "paper": "[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)",
        "description": "Standard CLIP uses a symmetric cross-entropy InfoNCE loss over a global batch similarity matrix to maximize matched image-caption pairs and minimize unmatched pairs.",
        "mermaid": """graph TD
    I[Image Batch] --> IE[Image Encoder]
    T[Text Batch] --> TE[Text Encoder]
    IE --> Matrix[N x N Similarity Matrix]
    TE --> Matrix
    Matrix --> SymmetricCrossEntropy[Symmetric InfoNCE Loss]"""
    },
    {
        "filename": "siglip_pairwise.md",
        "title": "SigLIP (Sigmoid Pairwise Learning)",
        "year": "2023",
        "paper": "[Sigmoid Loss for Language-Image Pre-training](https://arxiv.org/abs/2303.15343)",
        "description": "In contrast to global normalization, SigLIP trains on pairwise binary logistic classification, solving scaling bottleneck and performance issues under limited VRAM.",
        "mermaid": """graph TD
    Img[Image Embeddings] --> Dot[Pairwise Dot Product]
    Txt[Text Embeddings] --> Dot
    Dot --> Logits[Logits Grid]
    Logits --> Sigmoid[Sigmoid Binary Loss]"""
    },
    {
        "filename": "multilingual_clip.md",
        "title": "Multilingual CLIP (mCLIP)",
        "year": "2022",
        "paper": "[Cross-lingual and Multilingual CLIP](https://aclanthology.org/2022.lrec-1.742/)",
        "description": "Multilingual CLIP replaces or aligns the text encoder with multi-lingual transformers, expanding zero-shot capabilities to dozens of languages.",
        "mermaid": """graph TD
    MultilingualText[Multilingual Text Input] --> MEncoder[Multilingual Text Encoder (e.g. XLM-R)]
    Image[Image] --> VEncoder[Visual Encoder]
    MEncoder --> CrossModal[Cross-Modal Alignment]
    VEncoder --> CrossModal"""
    },
    {
        "filename": "region_based_clip.md",
        "title": "Dense / Region-Based CLIP (RO-CLIP / OWL-ViT Style)",
        "year": "2022",
        "paper": "[Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230)",
        "description": "Modifies the image encoder to output dense, region-level visual representations, enabling localized object detection and open-vocabulary spatial grounding.",
        "mermaid": """graph TD
    Image[Image] --> VisionBackbone[Vision Transformer / ResNet]
    VisionBackbone --> RegionProposals[Region / Patch Features]
    TextQueries[Text Queries] --> TextEncoder[Text Encoder]
    RegionProposals --> Alignment[Region-Text Similarity Math]
    TextEncoder --> Alignment
    Alignment --> BoundingBoxes[Labeled Bounding Boxes]"""
    },
    {
        "filename": "vit_backed_clip.md",
        "title": "ViT-Backed CLIP (Transformer Dominant)",
        "year": "2021",
        "paper": "[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)",
        "description": "Uses a Vision Transformer (ViT) as the visual backbone, dividing input images into patches and using self-attention to process global spatial relationships.",
        "mermaid": """graph LR
    Image[Image] --> Patches[Patch Extraction]
    Patches --> LinearProj[Linear Projection & Position Embeddings]
    LinearProj --> ViT[ViT Transformer Blocks]
    ViT --> Output[Global Visual Representation]"""
    },
    {
        "filename": "cnn_backed_clip.md",
        "title": "CNN-Backed CLIP (ResNet Dominant)",
        "year": "2021",
        "paper": "[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)",
        "description": "Employs convolutional neural networks like ResNet to extract hierarchical visual features before projecting them to the cross-modal embedding space.",
        "mermaid": """graph LR
    Image[Image] --> ConvLayers[Hierarchical Convolutional Layers]
    ConvLayers --> Pooling[Global Pooling]
    Pooling --> Projection[Projection Layer]
    Projection --> Output[Contrastive Visual Embedding]"""
    },
    {
        "filename": "cross_modal_projection.md",
        "title": "Cross-Modal Projection Heads",
        "year": "2020",
        "paper": "[A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)",
        "description": "Small linear or MLP projection layers that map unimodal visual and text encoder states into a joint embedding space for contrastive training.",
        "mermaid": """graph TD
    VHidden[Vision Encoder Output] --> VProj[Vision MLP Projection Head]
    THidden[Text Encoder Output] --> TProj[Text MLP Projection Head]
    VProj --> Shared[Shared Semantic Space (e.g. 512-dim)]
    TProj --> Shared"""
    },
    {
        "filename": "data_curation_poisoning.md",
        "title": "The Data Curation and Poisoning Bottleneck",
        "year": "2023",
        "paper": "[Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149)",
        "description": "Mitigating dataset issues such as alt-text noise and adversarial split-view/frontrunning data poisoning using data filtering pipelines (e.g. LAION aesthetic filters) or robust training objectives.",
        "mermaid": """graph TD
    RawData[Raw Web Scraped Data] --> DataFiltering[Data Filtering Pipeline (Aesthetic / Text Quality)]
    DataFiltering --> CleanData[Clean Image-Text Pairs]
    CleanData --> RobustTraining[Contrastive Pre-training]"""
    },
    {
        "filename": "spatial_detail_blurring.md",
        "title": "The Spatial Detail Blurring Limit",
        "year": "2023",
        "paper": "[Segment Anything](https://arxiv.org/abs/2304.02643)",
        "description": "Standard CLIP models downsample images, losing fine-grained visual/textual details. Mitigated by using high-resolution AnyRes patching or combining with dense spatial models (e.g. SAM).",
        "mermaid": """graph TD
    HighResImage[High-Resolution Image] --> Patching[AnyRes / Patch Decomposition]
    Patching --> SubPatches[Sub-image Patches]
    SubPatches --> CLIPEncoder[CLIP Image Encoder]
    CLIPEncoder --> DenseFeatures[Detailed Spatial Embeddings]"""
    },
    {
        "filename": "ecommerce_categorization.md",
        "title": "Open-Vocabulary Zero-Shot E-Commerce Categorization",
        "year": "2021",
        "paper": "[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)",
        "description": "Using CLIP's zero-shot classification capabilities to automatically map marketplace seller product images to arbitrary natural language category strings dynamically.",
        "mermaid": """graph TD
    ProdImg[Seller Product Photo] --> VisionTower[CLIP Vision Tower]
    Categories[Natural Language Categories] --> TextTower[CLIP Text Tower]
    VisionTower --> ProdEmbed[Product Embedding]
    TextTower --> CatEmbeds[Category Embeddings]
    ProdEmbed --> Match[Similarity Search / Dot Product]
    CatEmbeds --> Match
    Match --> BestCategory[Assigned Category Label]"""
    },
    {
        "filename": "generative_guidance_diffusion.md",
        "title": "Text-to-Image Generative Guidance Models (Diffusion Frontends)",
        "year": "2022",
        "paper": "[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)",
        "description": "Utilizing CLIP's text encoder to align generative latent spaces. The text embedding directs the denoising U-Net matrix to synthesize matching graphics.",
        "mermaid": """graph TD
    Prompt[User Prompt] --> CLIPText[CLIP Text Encoder]
    CLIPText --> TextEmbedding[Text Conditioning Vector]
    TextEmbedding --> UNet[Denoising U-Net Matrix]
    LatentNoise[Latent Noise] --> UNet
    UNet --> Image[Synthesized Output Image]"""
    },
    {
        "filename": "multimodal_semantic_search.md",
        "title": "Enterprise Multi-Modal Semantic Search Engines",
        "year": "2021",
        "paper": "[CLIP4Clip: An Empirical Study of CLIP for Video Text Retrieval](https://arxiv.org/abs/2104.08860)",
        "description": "Indexing corporate video/photo assets in a joint vector space to allow complex natural language query matching and real-time retrieval without manual tagging.",
        "mermaid": """graph TD
    Assets[Video / Image Database] --> OffLineIndex[CLIP Feature Extraction & Indexing]
    OffLineIndex --> VectorDB[(Vector Database)]
    UserQuery[Natural Language Search Query] --> CLIPText[CLIP Text Encoder]
    CLIPText --> QueryEmbed[Query Embedding]
    QueryEmbed --> Search[Vector Search Engine]
    VectorDB --> Search
    Search --> RankedResults[Ranked Visual Assets]"""
    }
]

for topic in topics:
    filepath = os.path.join(details_dir, topic["filename"])
    content = f"""# {topic["title"]}

## Overview
{topic["description"]}

## Architecture & Workflow
Below is a diagram representing the system flow:

```mermaid
{topic["mermaid"]}
```

## First Used
- **Year:** {topic["year"]}
- **Paper:** {topic["paper"]}

[Back to Awesome-CLIP README](../README.md)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("All 15 detailed pages have been successfully created.")
