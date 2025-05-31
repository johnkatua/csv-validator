# CSV-Validator

A dynamic, multi-team CSV validation tool to verify data integrity after ETL pipelines.

## Features

- Validates only specified columns
- Rename columns dynamically using mapping
- Apply value transformations (TRUE -> Y, etc.)
- Support multiple profile/configs

## Usage

```bash
python script/cli.py --profile <profile-name>
```