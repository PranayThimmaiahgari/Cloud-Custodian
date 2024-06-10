import json
import boto3
import logging
import csv
import os
from io import StringIO
from botocore.exceptions import BotoCoreError, ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create_csv(resources):
    """Create a CSV file from the resources and return the file path."""
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    
    # Assuming resources is a list of dictionaries
    if resources:
        header = resources[0].keys()
        csv_writer.writerow(header)
        for resource in resources:
            csv_writer.writerow(resource.values())

    csv_buffer.seek(0)
    return csv_buffer.getvalue()

def lambda_handler(event, context):
    # Log the entire event
    logger.info(f"Received event: {json.dumps(event)}")

    # Create a new SES client
    REGION = 'us-east-1'
    ses_client = boto3.client('ses', region_name=REGION)
    logger.info(f"SES client created in region: {REGION}")

    success_count = 0
    failure_count = 0

    for record in event['Records']:
        try:
            # Extract message body from the SQS message
            message_body = record['body']
            logger.info(f"Message body: {message_body}")

            # Parse the JSON message
            message = json.loads(message_body)
            logger.info(f"Parsed message: {message}")

            # Extract email details from the message
            sender_email = message["policy"]["actions"][0]["transport"]["sender_email"]
            receiver_email = message["policy"]["actions"][0]["transport"]['receiver_email']
            subject = message["policy"]["actions"][0]["transport"]['subject']
            resources = message["resources"]
            body_text = message["policy"]["actions"][0]["transport"]["body_text"]

            # Create CSV file from resources
            csv_data = create_csv(resources)
            csv_attachment = MIMEBase('application', 'octet-stream')
            csv_attachment.set_payload(csv_data)
            encoders.encode_base64(csv_attachment)
            csv_attachment.add_header('Content-Disposition', 'attachment', filename='resources.csv')

            # Create a multipart/mixed parent container
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email

            # Add the body text and the CSV attachment to the message
            msg.attach(MIMEText(body_text, 'plain'))
            msg.attach(csv_attachment)

            # Send the email using SES
            response = ses_client.send_raw_email(
                Source=sender_email,
                Destinations=[receiver_email],
                RawMessage={'Data': msg.as_string()}
            )

            # Log the SES response
            logger.info(f"SES response: {response}")
            success_count += 1

        except KeyError as e:
            logger.error(f"Missing key in the message: {e}, Record: {record}")
            failure_count += 1
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}, Record: {record}")
            failure_count += 1
        except (BotoCoreError, ClientError) as e:
            logger.error(f"Boto3 error: {e}, Record: {record}")
            failure_count += 1
        except Exception as e:
            logger.error(f"Error processing message: {e}, Record: {record}")
            failure_count += 1

    logger.info(f"Successfully processed {success_count} messages, failed to process {failure_count} messages.")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Email processing completed.',
            'success_count': success_count,
            'failure_count': failure_count
        })
    }
