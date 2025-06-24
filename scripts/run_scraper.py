import sys
import os
import asyncio

# Add the parent directory of src to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.telegram_ingestion import client, start_scraping

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(start_scraping())
