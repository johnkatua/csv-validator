import logging
import pandas as pd

logger = logging.getLogger()

def read_csvs(source_path, target_path, config):
    try:
        df_source = pd.read_csv(source_path)
        df_target = pd.read_csv(target_path)
        print(df_source, df_target)
        
    except Exception as e:
        logger.error(f"Error comparing CSVs: {e}")
        print(f"Error: {e}")
        return False
