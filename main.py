import argparse
import yaml
import os
from src.csv_handler.load import read_csvs
from src.sf_extractor import connect_to_salesforce

def load_profile(profile_name):
    profile_path = f"profiles/{profile_name}.yaml"
    try:
        if not os.path.exists(profile_path):
            raise FileNotFoundError(f"Profile {profile_name} not found in 'profiles/'")
        with open(profile_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(e)
    
def main():
    parser = argparse.ArgumentParser(description="CSV Validator Tool")
    parser.add_argument("--profile", required=True, help="Profile name (without .yaml)")
    # parser.add_argument("--env", choices=["qa", "fullcopy", "docqa"], required=True, help="Salesforce environment")
    args = parser.parse_args()

    config = load_profile(args.profile)

    # sf = connect_to_salesforce(args.env)
    print(config)
    read_csvs(config)
    validator = True

    # Example query
    # result = sf.query("SELECT Id, Name FROM Account LIMIT 5")

    # for record in result.get("records", []):
    #     print(record["Name"])

    # if validator:
    #     print("Validation passed.")
    # else:
    #     print("Validation failed.")

if __name__ == "__main__":
    main()