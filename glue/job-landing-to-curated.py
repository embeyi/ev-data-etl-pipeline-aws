import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
import re

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init('job-landing-to-curated')

# Hardcoded S3 paths
s3_input_path = 's3://aws-s3-dap-landing-dev/electric_vehicle_data_wa_gov/api_views_f6w7-q2d2_rows.csv'
s3_output_path_type_bev = 's3://aws-s3-dap-curated-dev/Battery_Electric_Vehicle-BEV/'
s3_output_path_type_phev = 's3://aws-s3-dap-curated-dev/Plug-in_Hybrid_Electric_Vehicle-PHEV/'

input_df = spark.read.format("csv").option("header", "true").load(s3_input_path)

input_df = input_df.toDF(*(re.sub(r'[\(\)\-0-9]', '', col.replace(' ', '_')) for col in input_df.columns))

type_a_df = input_df.filter(col('Electric_Vehicle_Type') == 'Plug-in Hybrid Electric Vehicle (PHEV)')
type_b_df = input_df.filter(col('Electric_Vehicle_Type') == 'Battery Electric Vehicle (BEV)')

type_a_df.coalesce(1).write.format("csv").option("header", "true").mode("overwrite").save(s3_output_path_type_phev)
type_b_df.coalesce(1).write.format("csv").option("header", "true").mode("overwrite").save(s3_output_path_type_bev)
job.commit()
