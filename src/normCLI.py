import requests
import json
import urllib
import ast

def checkAdd(y):
	accepted_types = ['[["street_address"]]', '[["subpremise"]]']
	r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+y+'&sensor=false')
	if r.json['status'] == "OK":
		for x in r.json['results']:
			if json.dumps([x['types']]) in accepted_types:
				return json.dumps( {"status": "OK", "address": [x['formatted_address']]} )
				break
			else:
				return json.dumps( {"status": "INCOMPLETE", "address": [x['formatted_address']]} )
				break
	else:
		return json.dumps( {"status": "INVALID"} )

def checkList():		
	with open("addresses.txt", "r") as f:
		lines = f.readlines()
		for x in lines:
			y = ast.literal_eval(x)
			data_join = ' '.join(y)
			data_pack = urllib.quote_plus(data_join)
			print checkAdd(data_pack)
	f.close()

if __name__ == "__main__":
	checkList()