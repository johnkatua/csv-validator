# CSV-Validator

A dynamic, multi-team CSV validation tool to verify data integrity after ETL pipelines.

## Features

- Validates only specified columns
- Rename columns dynamically using mapping
- Apply value transformations (TRUE -> Y, etc.)
- Support multiple profile/configs
- Extracts data from Salesforce using SOQL
- Generates differences report if mismatch found
- Logs all activity for easy debugging

## Setup
1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python script/cli.py --profile <profile-name> -- env <env>
```