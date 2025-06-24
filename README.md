# 📦 EthioMart: Amharic Named Entity Recognition for Telegram E-Commerce

## 🧾 Project Overview

**EthioMart** is an AI-driven initiative that aims to unify Ethiopia's growing Telegram-based e-commerce landscape into a centralized platform. As independent sellers increasingly use Telegram to promote and sell products, customers face the challenge of discovering and comparing products spread across dozens of decentralized channels.

This project solves that challenge by **automatically extracting key product details**—like product names, prices, and locations—from **Amharic messages, images, and documents** posted in Telegram groups. These entities are identified using a fine-tuned **Named Entity Recognition (NER)** model built on top of multilingual transformer models like XLM-Roberta or Amharic-specific models.


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