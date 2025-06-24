import os
import pandas as pd
import re

RAW_PATH = "data/raw/telegram_data.csv"
OUTPUT_PATH = "data/processed/preprocessed_telegram.csv"

# Make sure output directory exists
os.makedirs("data/processed", exist_ok=True)

def clean_text(text):
    if pd.isna(text) or text.strip() == "":
        return None
    # Remove Telegram links, phone numbers, emojis, unwanted characters
    text = re.sub(r"http\S+|www\S+|t.me\S+", "", text)  # remove links
    text = re.sub(r"[^\w\s፣።፤፥፦፡፠መሃል]+", "", text)  # remove emojis & Latin punctuations
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    return text.strip()

def preprocess_telegram_data():
    df = pd.read_csv(RAW_PATH)
    df.drop_duplicates(subset=["Message"], inplace=True)
    df["Message"] = df["Message"].apply(clean_text)
    df.dropna(subset=["Message"], inplace=True)
    df = df[df["Message"].str.len() > 10]  # filter very short messages
    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"[✓] Preprocessed data saved to {OUTPUT_PATH}")
