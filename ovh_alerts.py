#!/usr/bin/python3

import json
import ovh
import time
import requests

client = ovh.Client(
	endpoint='ovh-eu',
	application_key='KEY',
	application_secret='SECRET',
	consumer_key='KEY',
)

ips = [
	['Web Server', '51.4.3.2', 'https://discord.com/api/webhooks/...', False]
]

def discord(label, mitigation, url):
	data = {
		'username': 'Firewall'
	}

	if mitigation:
		data['embeds'] = [
			{
				'title': 'Detección de un ataque',
				'description': 'Se ha detectado un ataque sobre el servicio **' + label + '**.',
				'color': 16056320
			}
		]
	else:
		data['embeds'] = [
			{
				'title': 'Fin del ataque',
				'description': 'Se ha dejado de detectar un ataque sobre el servicio **' + label + '**.',
				'color': 65338
			}
		]
	result = requests.post(url, json = data)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)

if __name__ == '__main__':
	while True:
		for ip in ips:
			try:
				response = client.get('/ip/' + ip[1] + '/mitigation/' + ip[1])

				print(ip[0] + ' (' + ip[1] + ') -> ' + str(response['auto']))
				if ip[3] == False and response['auto'] == True:
					discord(ip[0], True, ip[2])
					ip[3] = True
				elif ip[3] == True and response['auto'] == False:
					discord(ip[0], False, ip[2])
					ip[3] = False
			except:
				print(ip[0] + ' (' + ip[1] + ') -> An exception occurred')
		time.sleep(120)
