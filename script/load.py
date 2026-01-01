import pandas as pd
from sqlalchemy import create_engine
from script.logger import logger
from script.config import DB_CONFIG
from script.transform import output_path

csv_path = output_path

def load_carts(csv_path):
  try:
    logger.info('Starting Loading Data')
    engine = create_engine(
      f'postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}'
      f'@{DB_CONFIG["host"]}:{DB_CONFIG["port"]}/{DB_CONFIG["database"]}'
    )
    df = pd.read_csv(csv_path)
    df.to_sql(
      name = 'carts',
      con = engine,
      if_exists = 'append',
      index = False
    )
    logger.info(f'Loaded {len(df)} records into database')
  except Exception as e:
    logger.error(f'Load failed: {e}')
    raise
