import requests
import json


def curl_request(message, user):
	headers = {
	'Content-Type': 'application/json',
	}

	# Later change to every user
	data = '{"sender": " '+ user +'","message": "' + message + '","metadata": {}}'
	response = requests.post('http://localhost:5055/webhook', headers=headers, data=data)
	messages = json.loads(response.content)
	answer = list(map(lambda msg: msg['image'] if 'image' in msg else msg['text'], messages))

	return answer
