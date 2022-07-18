# Text Normalizer

Tool for cleaning and normalizing text for speech related NLP tasks

---

## Installation

To install directly into your current environment use pip

```bash
python3 -m pip install git+https://github.com/NewSciTLH/text-normalizer.git
```

To add text-normalizer as a dependency in other projects:

**setuptools**
add the following line to a __requirements.txt__ file
```bash
git+https://github.com/NewSciTLH/text-normalizer.git
```

**poetry**
add the following line in the __[tool.poetry.dependencies]__ section of __pyproject.toml__
```bash
text-normalizer = { git = "ssh://git@github.com/NewSciTLH/text-normalizer.git", branch = "prod" }
```

## Development

If you want to contribute to this project you will need to use the build process.
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
import pandas as pd

# Create instance of text normalizer
tn = TextNormalizer()

# TextNormalizer accepts various objects containing text
text = """Some string of text!"""
norm_text = tn(text)

text = ["123", "They're here"]
norm_text = tn(text)

text = set(text)
norm_text = tn(text)

text = pd.Series(list(text))
norm_text = tn(text)
```

As a further example, run the _main.py_ file.

## License

TextNormalizer has a BSD-style license. It can be found in the LICENSE file.
