 EthioMart Amharic E-commerce Data Extractor

Transforming messy Telegram posts into a smart FinTech engine that reveals the best vendors for micro-lending through Named Entity Recognition (NER) on Amharic text.

---

## 📖 Project Overview

EthioMart aims to become Ethiopia’s primary centralized hub for Telegram-based e-commerce activities by consolidating real-time data from multiple Telegram channels into a unified platform. This project focuses on developing a robust pipeline that:

- Ingests and preprocesses Amharic e-commerce messages from multiple Telegram channels.
- Labels key entities such as Product Names, Prices, and Locations in Amharic text.
- Fine-tunes transformer-based NER models (e.g., XLM-Roberta) to accurately extract entities.
- Compares multiple models and evaluates their performance.
- Uses interpretability tools (SHAP, LIME) to explain model predictions.
- Computes vendor metrics and a lending score to identify promising micro-lending candidates.

---

## 🎯 Key Objectives

- Build an end-to-end data ingestion and preprocessing pipeline for Ethiopian Telegram e-commerce data.
- Label a high-quality Amharic NER dataset in CoNLL format.
- Fine-tune and evaluate multilingual transformer models for Amharic NER.
- Interpret model predictions to ensure transparency and trust.
- Analyze vendor activity and calculate lending scores to support EthioMart’s financial goals.

---

## 🗂️ Project Structure

ethioMart-NER/
├── config/
│ └── telegram_channels.json # Telegram channel configs
├── data/
│ ├── raw/ # Raw scraped Telegram data
│ ├── processed/ # Cleaned and tokenized data
│ └── labeled/ # CoNLL formatted labeled data
├── photos/ # Product images and marketing materials
├── scripts/
│ ├── run_scraper.py # Telegram scraping tool
│ └── run_preprocessing.py # Text cleaning and preprocessing scripts
├── src/
│ ├── preprocessing.py # Text preprocessing utilities
│ ├── telegram_ingestion.py # Telegram data ingestion modules
│ ├── ner_utils.py # NER dataset processing helpers
│ └── utils.py # Miscellaneous utility functions
├── training/
│ ├── amharic_ner_finetune.ipynb # Colab notebook for model fine-tuning
│ ├── saved_models/ # Directory for saved fine-tuned models
│ └── interpretability/ # Scripts and reports for model interpretability
│ ├── shap_explainer.py
│ ├── lime_explainer.py
│ └── interpretability_report.md
├── .gitignore
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .env # Environment variables (ignored)
└── config.json # Configuration file for training parameters


⚙️ Setup Instructions
1. Clone the Repo

git clone https://github.com/Oliyadm/ethioMart-NER.git
cd ethioMart-NER
2. Create and Activate Virtual Environment

python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Telegram API Credentials
Create a .env file based on the .env.example and add:

TG_API_ID=your_telegram_api_id
TG_API_HASH=your_telegram_api_hash
phone=+2519xxxxxxxx

