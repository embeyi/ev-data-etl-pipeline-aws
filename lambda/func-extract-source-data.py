import json
import os
import boto3
import requests
from datetime import datetime
from urllib.parse import urlparse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # List of API URLs
        api_urls = [
            'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
            # 'https://data.wa.gov/api/views/3d5d-sdqb/rows.csv?accessType=DOWNLOAD'
            # Add more URLs as needed 
        ]
        
        bucket_name = 'aws-s3-dap-landing-dev'
        
        for api_url in api_urls:
            try:
                # Fetch the data from the API
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    data = response.content
                    
                    # Parse the URL to create a unique folder name based on the domain and path  
                    parsed_url = urlparse(api_url)
                    domain = parsed_url.netloc.replace('.', '_')
                    path = parsed_url.path.replace('/', '_').strip('_')
                    
                    # Define the S3 object key (folder structure) 
                    file_name = f"electric_vehicle_{domain}/{path}"
                    
                    # Upload the file to S3
                    s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
                    
                    print(f"File uploaded successfully to {bucket_name}/{file_name}")
                else:
                    print(f"Failed to fetch data from the API: {api_url}, Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from API {api_url}: {e}")
            except boto3.exceptions.Boto3Error as e:
                print(f"Error uploading file to S3: {e}")
        
        return {
            'statusCode': 200,
            'body': json.dumps("Files uploaded successfully")
        }
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps("An error occurred during execution")
        }
