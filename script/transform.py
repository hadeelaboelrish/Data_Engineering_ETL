import pandas as pd
import json
from script.logger import logger
from script.config import PROCESSED_DATA_PATH
from script.extract import file_path

raw_file_path = file_path

def transform_carts (raw_file_path):
  logger.info('Starting Data Transformation')
  with open(raw_file_path) as f:
    data = json.load(f)
    rows = []
    
    for cart in data:
      for product in cart["products"]:
        rows.append({
            "cart_id": cart["id"],
            "user_id": cart["userId"],
            "product_id": product["id"],
            "product_name": product["title"],
            "quantity": product["quantity"],
            "price": product["price"],
            "total": product["total"]
        })


        output_path = PROCESSED_DATA_PATH + "orders_clean.csv"
        df.to_csv(output_path, index=False)

        logger.info(f"Transformed {len(df)} rows")
        return output_path

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
      
