"""
Logging utility
"""

import logging
import os

def setup_logger(config):
    config_logger = config['logging']
    log_file = config_logger['log_file']
    level = config_logger['level'].upper()
    log_level = getattr(logging, level, logging.INFO)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    return logging.getLogger()