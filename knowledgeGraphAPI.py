"""Example of Python client calling Knowledge Graph Search API."""

### Use a company name to retrieve a company domain
import json
import urllib

api_key = 'AIzaSyCTVEnopRQIgUkS0BunQ3pQFq64FnYP2O4'
query = 'Emerica'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())


for element in response['itemListElement']:
  if 'url' in element['result'].keys():
  	if element['result']['name'] == query:
  		print element['result']['url']

