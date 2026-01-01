import requests
import json
from datatime import datetime
from script.logger import logger
from script.config import API_URL, RAW_DATA_PATH


def extract_products():
  try:
    logger.info('Starting Data Extraction')
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    file_name = f'products_{datetime.now().date()}.json'
    file_path = RAW_DATA_PATH + file_name
    with open(file_path, 'w') as f:
      json.dump(data, f)
    logger.info(f'Extracted {len(data)} records')
    return file_path
  except Exception as e:
    logger.error(f"Extraction failed: {e}")
    raise
