import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
from random import shuffle

# This key will serve all examples in this document.
KEY = "41dafc9506654c6fa8f2c8ceb91e3ea7"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://gotofaces.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

img = Image.open('faces4.jpeg')

print(img.size)

detected_faces = face_client.face.detect_with_stream(image=open('faces4.jpeg', 'rb'))

faces = []

for face in detected_faces:
    print (face)
    rect = face.face_rectangle
    print(rect)
    faces.append(img.crop((rect.left, rect.top, rect.left + rect.width, rect.top + rect.height)))

for face in faces:
    face.show()

shuffle(faces)

for i in range(len(detected_faces)):
    rect = detected_faces[i].face_rectangle
    faces[i].resize((rect.width, rect.height))
    img.paste(faces[i], (rect.left, rect.top))

img.show()