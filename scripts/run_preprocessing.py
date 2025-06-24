import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import preprocess_telegram_data


if __name__ == "__main__":
    preprocess_telegram_data()
