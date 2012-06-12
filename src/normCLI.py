import requests, json, urllib, ast
from operator import itemgetter

class addObj:
	def __init__(self, status = None, street_number = None, subpremise = None, street = None, city = None, state = None, zipcode = None, country = None):
		self.status = status
		self.street_number = street_number
		self.subpremise = subpremise
		self.street = street
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.country = country
	
	def printAdd(self):
		print 'Status: \t', self.status
		print 'Street Number: \t', self.street_number
		print 'Street: \t', self.street
		print 'Subpremise: \t', self.subpremise
		print 'City: \t\t', self.city
		print 'State: \t\t', self.state
		print 'Zipcode: \t', self.zipcode
		print 'Country: \t', self.country
		
	def jsonAdd(self):
		return json.dumps( {"status": self.status, "street_number": self.street_number, "street": self.street, "subpremise": self.subpremise, "city": self.city, "state": self.state, "zipcode": self.zipcode, "country": self.country} )


def checkAdd(y):
	accepted_types = ['street_address', 'subpremise']
	r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+y+'&sensor=false')
	newAddress = addObj()
	
	# TODO: Less messy way of getting the values for Google's return JSON values?
	if r.json['status'] == "OK":
		addTypes = map(itemgetter('types'), r.json['results'])
		if addTypes[0][0] in accepted_types:
			newAddress.status = "OK"
		else:
			newAddress.status = "INCOMPLETE"
			
		addComp = map(itemgetter('address_components'), r.json['results'])
		for x in range(len(addComp[0])):
			# In case Google decides to give us an empty list..
			addType = addComp[0][x].get('types')
			if not addType:
				continue
			else:
				addType = addType[0]
				
			# Separate our information and save.
			if addType == "street_number":
				newAddress.street_number = addComp[0][x].get('long_name')
			elif addType == "administrative_area_level_1":
				newAddress.state = addComp[0][x].get('long_name')
			elif addType == "country":
				newAddress.country = addComp[0][x].get('long_name')
			elif addType == "postal_code":
				newAddress.zipcode = addComp[0][x].get('long_name')
			elif addType == "route":
				newAddress.street = addComp[0][x].get('long_name')
			elif addType == "locality":
				newAddress.city = addComp[0][x].get('long_name')
			elif addType == "subpremise":
				newAddress.subpremise = addComp[0][x].get('long_name')
				
	else:
		newAddress.status = "INVALID"
	return newAddress

def checkList():		
	with open("addresses.txt", "r") as f:
		lines = f.readlines()
		for x in lines:
			y = ast.literal_eval(x)
			data_join = ' '.join(y)
			data_pack = urllib.quote_plus(data_join)
			newAddress = checkAdd(data_pack)
			print newAddress.jsonAdd()
	f.close()

if __name__ == "__main__":
	checkList()
