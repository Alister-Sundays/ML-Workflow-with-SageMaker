import json

THRESHOLD = 0.93  # Adjust the threshold as needed

def lambda_handler(event, context):
    """Filters inferences based on a confidence threshold."""

    inferences = event['body']['inferences']

    # Check if any inference confidence exceeds the threshold
    meets_threshold = any(inference >= THRESHOLD for inference in inferences)

    # Raise an exception if the threshold is not met
    if not meets_threshold:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }