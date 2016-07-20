import requests

base_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3'
my_api_key = "{YOUR_API_KEY_HERE}"
payload = {'version':'2016-05-20', 'api_key':my_api_key}

classifier_id = "{YOUR_CLASSIFIER_ID_HERE}"

#GET CLASSIFIER DETAILS
response = requests.get(base_url+'/classifiers/'+classifier_id, params=payload)

print response.content
