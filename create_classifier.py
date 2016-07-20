import requests

base_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3'
my_api_key = "{YOUR_API_KEY_HERE}"
payload = {'version':'2016-05-20', 'api_key':my_api_key}

#A dictionary of the classes we want in the classifier with their zip files
files = {'hearts_positive_examples':open('hearts.zip'),
        'diamonds_positive_examples': open('diamonds.zip'),
        'clubs_positive_examples': open('clubs.zip'),
        'spades_positive_examples': open('spades.zip')}

classifier_name = {'name':"suits_classifier"}

#CREATE CLASSIFIER
response = requests.post(base_url + '/classifiers', files=files, \
    data=classifier_name, params=payload)

print response.content
