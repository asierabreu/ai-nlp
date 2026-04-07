# 🔗 Shared Utilities

Reusable Python utilities, dataset loaders, and model wrappers shared across all
projects in this monorepo.

## Structure

```
shared/
├── utils/
│   ├── __init__.py
│   └── text.py             # Text preprocessing utilities
├── datasets/
│   ├── __init__.py
│   └── loaders.py          # Dataset loading helpers
├── models/
│   ├── __init__.py
│   └── wrappers.py         # Pre-trained model wrappers
├── tests/
│   └── test_text_utils.py
├── requirements.txt
└── README.md
```

## Usage

```python
# Text utilities
from shared.utils.text import clean_text, tokenize

text = clean_text("  Hello,   World!  ")
tokens = tokenize(text)

# Dataset loaders
from shared.datasets.loaders import load_jsonl

dataset = load_jsonl("path/to/data.jsonl")

# Model wrappers
from shared.models.wrappers import EmbeddingModel

model = EmbeddingModel("sentence-transformers/all-MiniLM-L6-v2")
embedding = model.encode("Hello world")
```

## Installation

```bash
pip install -r shared/requirements.txt
```
