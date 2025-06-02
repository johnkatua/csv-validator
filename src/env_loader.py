import os
from dotenv import load_dotenv
import yaml

def load_env_config():
    with open("config/environments.yaml", "r") as f:
        return yaml.safe_load(f)
    

def get_dotenv_path(env):
    env_config = load_env_config()
    dotenv_file = env_config['environments'][env]['dotenv_file']
    dotenv_path = os.path.join(os.getcwd(), dotenv_file)

    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f"Environment file not found: {dotenv_path}")
    return dotenv_path

def load_salesforce_credentials(env):
    dotenv_path = get_dotenv_path(env)
    load_dotenv(dotenv_path)

    return {
        'username': os.getenv('SF_USERNAME'),
        'password': os.getenv('SF_PASSWORD'),
        'organizationId': os.getenv('SF_ORG_ID')
    }