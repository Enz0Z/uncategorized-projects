#!/usr/bin/python3

import json
import requests
import urllib.parse
from http.server import *
from urllib import parse

WEBHOOKS = {
	'NAME': 'https://discord.com/api/webhooks/...',
}

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		path = parse.urlparse(self.path)
		query = dict(urllib.parse.parse_qsl(path.query))
		ip = self.headers.get('CF-Connecting-IP')

		if 'key' in query and ip is not None:
			data = {}

			if 'content' in query:
				data['content'] = query['content'].replace('NEWLINE', '\n').replace('CLIENT_IP', ip)
			if 'embeds' in query:
				data['embeds'] = json.loads(query['embeds'].replace('NEWLINE', '\n').replace('CLIENT_IP', ip))
			result = requests.post(WEBHOOKS[query['key']], json = data)

			try:
				result.raise_for_status()
			except requests.exceptions.HTTPError as err:
				print(err)

		self.send_response(204)
		self.end_headers()

if __name__ == '__main__':
	HTTPServer(('localhost', 1337), handler).serve_forever()
