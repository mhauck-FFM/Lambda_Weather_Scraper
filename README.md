# Lambda Weather Scraper
The purpose of this simple program is to gather live weather data for a weather station in Frankfurt/Main (Germany) from a given website. Other websites can be easily added. The data on the website are updated once per hour, so we use an AWS Lambda function to run the program once every hour and store the data on AWS S3 as .json files.

### Program Structure

- `Weather_Scrape_Lambda.py`, contains the main function to gather the data from the website
- `lambda_function.py`, contains the main code for the Lambda function (enter your S3 bucket name)

#### Setup Instructions

Create a new Lambda layer on AWS that has access to both the defined functions as well as all listed python modules below. The easiest way to do this is to zip all modules together with the functions and upload them to AWS Lambda. You then setup a simple schedule for the AWS Lambda function by using AWS CloudWatch Events. 

#### Mandatory Python Modules

- boto3
- json
- beautiful soup
- requests
- datetime
- regular expressions
