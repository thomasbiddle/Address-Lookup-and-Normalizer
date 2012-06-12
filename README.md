Address-Lookup-and-Normalizer
=============================

Given input, works with Google Maps API and returns back a JSON formatted response as to whether the address is valid, and gives it's address portions.
<pre>
eg: {"status": "OK", "city": "Kansas City", "state": "Missouri", "street": "Broadway", "street_number": "600", "country": "United States", "subpremise": "400", "zipcode": "64105"}
</pre>

Also runs a web-service utilizing Flask. Information can be requested using the RESTful API via GET & POST.

<h3>Examples:</h3>

normFlask.py must be run in order to access the web-service

REST Interface - Accepted request methods: GET, POST
<pre>
root@Python:~/# curl localhost:5000 -d 'input=1955 Landings Drive CA'
{"status": "OK", "city": "Mountain View", "state": "California", "street": "Landings Dr", "street_number": "1955", "country": "United States", "subpremise": null, "zipcode": "94043"}
</pre>

When running normCLI.py directly, it will read from addresses.txt located in the same directly and will treat each line as input. Format for address.txt is a Python list ( eg: ['1955 Landings Drive', 'California', ''] )
<pre>
root@Python:~/# python normCLI.py
{"status": "OK", "city": "Kansas City", "state": "Missouri", "street": "Broadway", "street_number": "600", "country": "United States", "subpremise": "400", "zipcode": "64105"}
{"status": "INCOMPLETE", "city": "Los Angeles", "state": "California", "street": null, "street_number": null, "country": "United States", "subpremise": null, "zipcode": "90001"}
{"status": "OK", "city": "Charlotte", "state": "North Carolina", "street": "South Blvd", "street_number": "1900", "country": "United States", "subpremise": "304", "zipcode": "28203"}
{"status": "OK", "city": "Salt Lake City", "state": "Utah", "street": "Olympus View Dr", "street_number": "4217", "country": "United States", "subpremise": null, "zipcode": "84124"}
{"status": "OK", "city": "Oceanside", "state": "California", "street": "Serene Rd", "street_number": "1472", "country": "United States", "subpremise": null, "zipcode": "92057"}
{"status": "INCOMPLETE", "city": null, "state": null, "street": null, "street_number": null, "country": "Colombia", "subpremise": null, "zipcode": null}
....
</pre>

You can also call the checkAdd() function directly, passing it an address as a string.
<pre>
Python 2.7.3 (default, May  9 2012, 23:42:16)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import normCLI
>>> normCLI.checkAdd("1955 Landings Drive CA").jsonAdd()
'{"status": "OK", "city": "Mountain View", "state": "California", "street": "Landings Dr", "street_number": "1955", "country": "United States", "subpremise": null, "zipcode": "94043"}'
>>> normCLI.checkAdd("1955 Landings Drive CA").printAdd()
Status:         OK
Street Number:  1955
Street:         Landings Dr
Subpremise:     None
City:           Mountain View
State:          California
Zipcode:        94043
Country:        United States
</pre>