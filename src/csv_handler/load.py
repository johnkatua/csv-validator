import logging

logger = logging.getLogger()

def read_csvs(source_path, target_path, config):
    try:
        print('te')
    except Exception as e:
        logger.error(f"Error comparing CSVs: {e}")
        print(f"Error: {e}")
        return False
