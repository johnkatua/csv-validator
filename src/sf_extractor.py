from simple_salesforce import Salesforce
from src.env_loader import load_salesforce_credentials

def connect_to_salesforce(env):
    print(f"Connecting to Salesforce ({env.upper()})...")
    credentials = load_salesforce_credentials(env)
    print(credentials)

    try:
        sf = Salesforce(**credentials)
        print("Successfully connected to Salesforce!")
        return sf
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Salesforce: {e}")