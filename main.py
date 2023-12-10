import boto3
import pycountry

# Create a CloudFront client
client = boto3.client('cloudfront')

# Define your distribution ID and country allow list
distribution_id = 'YOUR_DISTRIBUTION_ID'
countries = ['Israel', 'Spain', 'Brazil']  # Example country

# Convert country names to ISO 3166-1 alpha-2 country codes
country_codes = [pycountry.countries.lookup(country).alpha_2 for country in countries]

# Get the current distribution configuration
response = client.get_distribution_config(Id=distribution_id)
dist_config = response['DistributionConfig']
etag = response['ETag']

# Modify the configuration to add geographic restrictions
geo_restriction = {
    'RestrictionType': 'whitelist',
    'Quantity': len(country_codes),
    'Items': country_codes
}
dist_config['Restrictions']['GeoRestriction'] = geo_restriction

# Update the distribution
client.update_distribution(DistributionConfig=dist_config, Id=distribution_id, IfMatch=etag)
