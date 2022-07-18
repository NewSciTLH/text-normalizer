# Text Normalizer

Tool for cleaning and normalizing text for speech related NLP tasks

---

## Installation

```bash
python3 -m pip install git+https://github.com/NewSciTLH/text-normalizer
```

## Build

In consideration of [PEP
517-518](https://snarky.ca/what-the-heck-is-pyproject-toml/) the new python
packaging library [Poetry](https://python-poetry.org/) is employed in this
project.

Create a virtual environment
```bash
poetry shell
```

Install all of the development and library dependencies
```bash
poetry install
```

Run the tests
```bash
poetry run pytest
```

Build both the sdist and wheel
```bash
poetry build
```

## Get Started

Create an instance of TextNormalizer and then pass it a string.

```python
from text_normalizer import TextNormalizer

# Create instance of text normalizer
tn = TextNormalizer()

# TextNormalizer accepts various objects containing text
text = """Some string of text!"""
norm_text = tn(text)

text = ["123", "They're here"]
norm_text = tn(text)

text = set(text)
norm_text = tn(text)

text = pd.Series(text)
norm_text = tn(next)
```

As a further example, run the _main.py_ file.

## License

TextNormalizer has a BSD-style license. It can be found in the LICENSE file.
