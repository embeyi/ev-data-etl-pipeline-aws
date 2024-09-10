# ev-data-etl-pipeline-aws
AWS-based ETL pipeline for electric vehicle data processing. It ingests, transforms, and loads data into a data warehouse using services like AWS Lambda, Glue, Athena and S3. The pipeline ensures data cleaning, validation, and enrichment for comprehensive analysis and reporting.

## AWS Lambda
 AWS Lambda function is designed to fetch CSV data from a URL provided by the US Gov API, process it, and store it in an Amazon S3 bucket.

Dataset Used:
Washington State Open Data Portal

- https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD

### Configurations 
The timeout for the AWS Lambda function was set to 1 min 59 seconds to ensure that the function has sufficient time to complete its tasks, especially given that it involves multiple steps such as making HTTP requests to fetch data from the US gov API, processing the data, and uploading it to an S3 bucket.

## S3
### Raw Zone: Landing Bucket (aws-s3-landing-dev)
Setup: Configure AWS S3 to store raw data ingested by Lambda. Split the datasets into three different folders
#### Reason: 
Provides a scalable and durable storage solution for raw data.

 ### Transformed Zone: Transformed Bucket (aws-s3-curated-dev)
 Use to store the CSV file from the (job_landing_to_curated) Glue Job
#### Reason: 
Provides a scalable and durable storage solution for curated data based on different data sets.

 ## AWS GLue
### Glue Job (job_landing_to_curated)
Setup: This AWS Glue task takes a single file from landing bucket, splits data into two files based on categories and does some column naming convention updates before saving in different folders for each type of data set in curated bucket.  


#### Reason: Converting these files to a better CSV simplifies data manipulation and analysis, making it more accessible for downstream processes such as data analytics, reporting, and machine learning.


## Glue Crawler 
### (landing-bucket-crawler)
Setup: Configure Glue Crawler to automatically discover data stored in S3 and populate the Glue Data Catalog.
Reason: Simplifies metadata management by automatically detecting schema changes and updating the data catalog.


### (curated-bucket-crawler)
Setup: Configure Glue Crawler to automatically discover data stored in S3 and populate the Glue Data Catalog.
Reason: Simplifies metadata management by automatically detecting schema changes and updating the data catalog.
