# 👨🏻‍🏫 Wikibert

This is an experimental weekend project for testing purposes.

## Overview

Wikibert is a project that aims to demonstrate text generation using Wikipedia data. It consists of two main components:
- A Python script (`get_data.py`) for fetching and saving Wikipedia pages.
- A Jupyter notebook (`wikibert.ipynb`) for training a text generation model using TensorFlow.

## get_data.py

The `get_data.py` script performs the following tasks:
- Fetches a Wikipedia page and its linked pages recursively up to a specified depth.
- Saves the content of each page into individual text files in a `data` folder.
- Sanitizes filenames to ensure compatibility with the file system.

## wikibert.ipynb

The `wikibert.ipynb` notebook includes the following steps:
- Loads and preprocesses text data from the saved Wikipedia pages.
- Builds and trains a GRU-based RNN model for text generation using TensorFlow.
- Saves model checkpoints during training.
- Generates text using the trained model.

## Usage

1. Run `get_data.py` to fetch and save Wikipedia pages.
2. Open `wikibert.ipynb` in Jupyter Notebook or Google Colab.
3. Follow the cells in the notebook to train the text generation model and generate text.

## Requirements

- Python 3.x
- `wikipedia-api` library
- TensorFlow
- Jupyter Notebook (for `wikibert.ipynb`)

## Installation

Install the required libraries using pip:
```bash
pip install wikipedia-api tensorflow
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
