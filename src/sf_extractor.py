from simple_salesforce import SalesforceAPI
from src.env_loader import load_salesforce_credentials

def connect_to_salesforce(env):
    print(f"Connecting to Salesforce ({env.upper()})...")
    credentials = load_salesforce_credentials(env)

    try:
        sf = SalesforceAPI(**credentials)
        print("Successfully connected to Salesforce!")
        return sf
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Salesforce: {e}")