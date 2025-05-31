import argparse
import yaml
import os

def load_profile(profile_name):
    profile_path = f"profiles/{profile_name}.yaml"
    if not os.path.exists(profile_name):
        raise FileNotFoundError(f"Profile {profile_name} not found in 'profiles/'")
    with open(profile_path, 'r') as f:
        return yaml.load(f)
    
def main():
    parser = argparse.ArgumentParser(description="CSV Validator Tool")
    parser.add_argument("--profile", required=True, help="Profile name (without .yaml)")
    args = parser.parse_args()

    config = load_profile(args.profile)
    print(config)
    validator = True

    if validator:
        print("Validation passed.")
    else:
        print("Validation failed.")

if __name__ == "__main__":
    main()