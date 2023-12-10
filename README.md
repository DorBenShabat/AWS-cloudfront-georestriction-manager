# CloudFront GeoRestriction Manager

This repository contains a Python script that automates the process of updating Amazon CloudFront distributions with geographic restrictions. It enables users to specify countries by name, which are then converted to their respective ISO 3166-1 alpha-2 country codes and used to update the CloudFront distribution settings.

## Prerequisites

- AWS CLI configured with the necessary permissions.
- boto3 and pycountry Python packages installed.
- Run aws configure in your terminal.
- Enter your AWS Access Key ID and Secret Access Key when prompted.
- Specify the default region name and output format as required.
  
## Features

- Convert country names to ISO 3166-1 alpha-2 codes
- Update CloudFront distribution to whitelist specified countries
- Use of Boto3 and Pycountry libraries for AWS CloudFront management and country code conversion

## Prerequisites

Before running this script, ensure you have the following:
- Python installed on your machine (preferably Python 3.8 or newer)
- AWS CLI configured with the necessary permissions
- `boto3` and `pycountry` Python packages installed

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/cloudfront-georestriction-manager.git
