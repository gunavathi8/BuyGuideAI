# BuyGuideAI: Ecomm-Assist 🛒🤖

BuyGuideAI: Ecomm-Assist is an AI-powered conversational shopping assistant that helps users discover and compare products from e-commerce platforms in real time. Its backbone is a RAG (Retrieval-Augmented Generation) pipeline, enabling intelligent and context-aware responses based on live product data.

## 🚀 Project Overview
The system extracts product data from major e-commerce websites (like Amazon, Flipkart, etc.), transforms it into embeddings, and stores it in a cloud-based vector database (AstraDB). This enables the assistant to answer user queries with relevant, up-to-date product details.

**At its core, the project combines:**

- ETL & ELT Pipelines → Data ingestion from e-commerce sites.
- BeautifulSoup (HTML Parsing) → Real-time product data scraping.
- LangChain → Document processing & embeddings creation.
- AstraDB Vector Store → Storage & retrieval of product embeddings.
- RAG-powered Assistant → Conversational interface for e-commerce guidance.

## 🔄 Workflow
1. Data Ingestion (ETL/ELT Pipeline)
   - Extract → Scrape product listings from e-commerce sites using BeautifulSoup.
   - Load → Store raw scraped data into a CSV file.
   - Transform → Process CSV data into LangChain documents.

2. Embeddings & Storage
   - Create embeddings from product documents using LangChain’s embedding models.
   - Store the embeddings in AstraDB (Vector DB) for efficient semantic search.

3. RAG Assistant
   - Queries are matched against stored embeddings.
   - Relevant context is retrieved and used to generate conversational answers.

## 📂 Project Structure
```
ECOMM-ASSIST/
│── .github/
│   └── workflows/              # GitHub Actions workflows (CI/CD)
│── ecomm/                      # venv
│── notebook/
│   └── test.ipynb              # Jupyter notebook for experiments
│── prod_assistant/             # Main project source code
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.yaml         # Configuration file
│   │
│   ├── etl/                    # Data ingestion & scraping pipeline
│   │   ├── __init__.py
│   │   ├── data_ingestion.py   # Data ingestion logic
│   │   └── data_scrapper.py    # Web scraping logic (BeautifulSoup, etc.)
│   │
│   ├── exception/              # Custom exception handling
│   │   ├── __init__.py
│   │   └── custom_exception.py
│   │
│   ├── logger/                 # Logging utility
│   │   ├── __init__.py
│   │   └── custom_logger.py
│   │
│   ├── prompt_library/         # Prompt templates for RAG assistant
│   │   └── __init__.py
│   │
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── config_loader.py    # Load & parse configs
│   │   └── model_loader.py     # Load embedding / LLM models
│   │
│   └── workflow/               # Workflow orchestration
│       └── __init__.py
│
│── static/                     # Static files (CSS, JS, assets)
│── templates/
│   └── index.html              # Frontend template (for UI)
│── test/
│   └── __init__.py             # Test suite
│
│── .env                        # Environment variables
│── .gitignore                  # Git ignore file
│── .python-version             # Python version manager file
│── commands.txt                # Command references / scripts
│── get_lib_versions.py         # Script to check library versions
│── main.py                     # Main entry point of the app
│── pyproject.toml              # Project dependencies & metadata
│── README.md                   # Project documentation
│── requirements.txt            # Python dependencies
│── scapper_ui.py               # UI layer for scraping workflow

```

## ⚙️ Tech Stack

**Core Language**
  - 🐍 Python – Main programming language

**Data Ingestion & Scraping**
  - BeautifulSoup (bs4) – HTML parsing & product data extraction
  - undetected-chromedriver (uc) – Stealth browser automation
  - Selenium – Web automation & interaction
    - By, Keys, ActionChains

**AI & NLP**
  - LangChain – Document transformation, embeddings & RAG pipeline
  - AstraDB (Vector DB) – Cloud-based vector store for semantic search
  - Groq LLM – High-speed inference engine for LLMs
  - Gemini LLM – Google’s large language model for conversational AI

**APIs & Backend**
  - FastAPI – Backend service framework
  - CORS Middleware – Cross-Origin Resource Sharing support

**User Interfaces**
  - Basic HTML + CSS – Lightweight frontend template
  - Streamlit – Interactive data exploration & assistant UI

**Deployement Workflow**
  - Docker – Containerization of services
  - AWS ECR (Elastic Container Registry) – Store and manage Docker images
  - AWS ECS Fargate – Serverless container orchestration (run without managing servers)
  - GitHub Actions – CI/CD automation (build, test, deploy pipeline)
  - pyproject.toml / requirements.txt – Dependency management