import logging
import pandas as pd
from .rename import rename_columns

logger = logging.getLogger()

def read_csvs(config):
    try:
        source_path = config['source_file']
        target_path = config['target_file']
        key_field = config['primary_key']
        df_source = pd.read_csv(source_path)
        df_target = pd.read_csv(target_path)

        # Rename columns to match
        rename_columns(df_source, config)

        # Set index
        # df_source = df_source.set_index(key_field)
        # df_target = df_target.set_index(key_field)

        # Filter common columns
        # transform_df(df_source, df_target, config)
        return df_source, df_target

        # print(df_source, df_target)
        
    except Exception as e:
        logger.error(f"Error comparing CSVs: {e}")
        print(f"Error: {e}")
        return False
