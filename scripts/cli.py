import argparse
import yaml
import os

def load_profile(profile_name):
    profile_path = f"profiles/{profile_name}.yaml"
    if not os.path.exists(profile_name):
        raise FileNotFoundError(f"Profile {profile_name} not found in 'profiles/'")
    with open(profile_path, 'r') as f:
        return yaml.load(f)