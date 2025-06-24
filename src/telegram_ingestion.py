import os
import csv
from telethon import TelegramClient
from dotenv import load_dotenv
from datetime import datetime

# Load API credentials
load_dotenv(".env")
api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
phone = os.getenv("phone")

# Constants
OUTPUT_CSV = "data/raw/telegram_data.csv"
CHANNELS = [
    "@AwasMart",
    "@Leyueqa",
    "@ethio_brand_collection",
    "@meneshayeofficial",
    "@nevacomputer"
]

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Initialize Telegram client
client = TelegramClient("scraping_session", api_id, api_hash)

# Scrape a single channel
async def scrape_channel(client, channel_username, writer):
    try:
        entity = await client.get_entity(channel_username)
        async for message in client.iter_messages(entity, limit=10000):
            if not message.message:  # Skip if empty
                continue
            writer.writerow([
                entity.title,
                channel_username,
                message.id,
                message.message.replace('\n', ' ').strip(),
                message.date.strftime("%Y-%m-%d %H:%M"),
                ""  # Media path skipped
            ])
        print(f"[✓] Done scraping {channel_username}")
    except Exception as e:
        print(f"[!] Failed to scrape {channel_username}: {e}")

# Main function to be called from run_scraper.py
async def start_scraping():
    await client.start(phone=phone)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Channel Title", "Channel Username", "ID", "Message", "Date", "Media Path"])
        for channel in CHANNELS:
            await scrape_channel(client, channel, writer)
