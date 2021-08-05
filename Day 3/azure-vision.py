from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "2fc7c1ac00f947d480329d5afa982550"
endpoint = "https://goto-vision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

answer = computervision_client.analyze_image("https://sun9-51.userapi.com/c5127/u7980360/133709343/w_a6c6258d.jpg", visual_features=['Description'])


print(answer.description.captions[0])