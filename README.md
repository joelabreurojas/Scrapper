<h1 align='center'>
    Scrapper
</h1>

<p align='center'>
    <em>A web scraper for academic research with Flask interface.</em>
</p>

<h6 align='center'>
    <a href="https://github.com/joelabreurojas/Scrapper/blob/main/LICENSE">
        <img alt='MIT License' src='https://img.shields.io/static/v1.svg?label=License&message=MIT&logoColor=d9e0ee&colorA=302d41&colorB=3094FF'/>
    </a>
</h6>

&nbsp;

### ✨ Overview

Scrapper is a Python-based web application for scraping and analyzing academic papers from SciELO. It provides both a CLI interface and a Flask web interface for searching, viewing, and managing research articles.

**Features:**

- Web interface for browsing research papers
- API endpoints for programmatic access
- Article metadata extraction and storage
- Bootstrap-based responsive UI

&nbsp;

### 🚀 Getting Started

#### Prerequisites

- Python 3.10+
- pip

#### Installation

Clone the repository:

```bash
git clone https://github.com/joelabreurojas/Scrapper.git
cd Scrapper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

&nbsp;

### 📖 Usage

#### Web Interface

Run the Flask application:

```bash
python run.py
```

Open your browser and navigate to `http://localhost:5000`.

#### CLI Usage

```python
from researcher.helpers.academic_search import search_papers

results = search_papers("machine learning")
for paper in results:
    print(paper.title)
```

&nbsp;

### 🏗️ Architecture

```
researcher/
├── controller/     # Business logic
├── helpers/        # Utility functions
├── models/         # Data models
├── routes/         # Flask routes
└── views/          # Templates and static files
```
