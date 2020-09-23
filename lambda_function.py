import json
import boto3
from datetime import datetime

from Weather_Scrape_Lambda import scrapeWeather

def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    print('[INFO] Request weather data from Frankfurt-Hoechst...')

    weather_data = scrapeWeather()

    BUCKET_NAME = ''

    DATE = str(datetime.strftime(datetime.today(), '%d_%m_%Y_%H_%M'))

    OUTPUT_NAME = f'weather_data_{DATE}.json'
    OUTPUT_BODY = json.dumps(weather_data)

    print(f'[INFO] Saving data to S3 bucket: {BUCKET_NAME} ...')

    s3.Bucket(BUCKET_NAME).put_object(Key = OUTPUT_NAME, Body = OUTPUT_BODY)

    print(f'[INFO] Job done at {DATE}')
