import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Serializes target data from S3."""

    # Extract S3 key and bucket from the event
    s3_key = event['s3_key']
    s3_bucket = event['s3_bucket']

    # Download the data from S3
    s3.download_file(s3_bucket, s3_key, '/tmp/image.png')

    # Base64 encode the image data
    with open('/tmp/image.png', 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # Return the event with the encoded image data
    return {
        'statusCode': 200,
        'body': {
            'image_data': image_data,
            's3_bucket': s3_bucket,
            's3_key': s3_key,
            'inferences': []
        }
    }
