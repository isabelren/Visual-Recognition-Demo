import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(2016-05-20, api_key='{YOUR_API_KEY_HERE}')

print(json.dumps(visual_recognition.get_classifier('YOUR CLASSIFIER ID'), indent=2))
