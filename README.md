# ev-data-etl-pipeline-aws
AWS-based ETL pipeline for electric vehicle data processing. It ingests, transforms, and loads data into a data warehouse using services like AWS Lambda, Glue, Athena and S3. The pipeline ensures data cleaning, validation, and enrichment for comprehensive analysis and reporting.

## AWS Lambda
 AWS Lambda function is designed to fetch CSV data from a URL provided by the US Gov API, process it, and store it in an Amazon S3 bucket.

Dataset Used:
Washington State Open Data Portal

'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
