import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='{YOUR_API_KEY_HERE}')

with open(join(dirname(__file__), './test1.jpg'), 'rb') as image_file:
 print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['{YOUR_CLASSIFIER_ID_HERE}']), indent=2))
