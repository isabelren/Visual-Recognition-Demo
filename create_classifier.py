import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='{YOUR_API_KEY_HERE}')

with open(join(dirname(__file__), 'hearts.zip'), 'rb') as hearts, \
    open(join(dirname(__file__), 'diamonds.zip'), 'rb') as diamonds, \
    open(join(dirname(__file__), 'clubs.zip'), 'rb') as clubs, \
    open(join(dirname(__file__), 'spades.zip'), 'rb') as spades :
 print(json.dumps(visual_recognition.create_classifier('Suits', \
    hearts_positive_examples=hearts, \
    diamonds_positive_examples=diamonds, \
    clubs_positive_examples=clubs, \
    spades_positive_examples=spades), indent=2))
