#!/usr/bin/python3

import json
import time
import requests
import psutil

WEBHOOK = 'https://discordapp.com/api/webhooks/...'
PROCESS = [
	['node core.js', 'server', False]
]

def check(name):
	for proc in psutil.process_iter(attrs = ['cmdline']):
		try:
			cmdline = ' '.join([str(elem) for elem in proc.info['cmdline']])

			if name == cmdline:
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False

def discord(process, retval):
	data = {
		'username': 'Process Check'
	}

	if retval:
		data['embeds'] = [
			{
				'title': process[1],
				'description': '**' + process[0] + '**',
				'color': 65338
			}
		]
	else:
		data['embeds'] = [
			{
				'title': process[1],
				'description': '**' + process[0] + '**',
				'color': 16056320
			}
		]
	result = requests.post(WEBHOOK, json = data)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)

if __name__ == '__main__':
	while True:
		for process in PROCESS:
			if not process[2] and check(process[0]):
				discord(process, True)
				process[2] = True
			elif process[2] and not check(process[0]):
				discord(process, False)
				process[2] = False
		time.sleep(15)
