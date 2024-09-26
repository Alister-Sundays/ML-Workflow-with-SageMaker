import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-endpoint"

def lambda_handler(event, context):

    # Decode the image data from the event payload
    image_data = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor for the specified endpoint
    predictor = Predictor(endpoint_name=ENDPOINT)

    # For this model, the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction on the image data
    inferences = predictor.predict(image_data)

    # We return the inferences back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    
    return {
        'statusCode': 200,
        'body': event['body']
    }
