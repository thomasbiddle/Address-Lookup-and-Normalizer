Address-Lookup-and-Normalizer
=============================

Given input, works with Google Maps API and returns back a JSON formatted response as to whether the address is valid, and gives it's full address.
eg: {"status": "OK", "address": ["600 Broadway #400, Kansas City, MO 64105, USA"]}

<h3>Examples:</h3>

normFlask.py must be run in order to access the web-service

REST Interface - Accepted request methods: GET, POST
<pre>
root@Python:~/PythonScripts/AddressNorm# curl localhost:5000 -X POST -d 'input="1955 Landings Drive CA"'
{"status": "OK", "address": ["1955 Landings Dr, Mountain View, CA 94043, USA"]}
</pre>

<pre>
http://localhost:5000/?input=%221955%20landings%20drive%22
</pre>

When running normCLI.py directly, it will read from addresses.txt located in the same directly and will treat each line as input. Format for address.txt is a Python list ( eg: ['1955 Landings Drive', 'California', ''] )
<pre>
root@Python:~/PythonScripts/AddressNorm# python normCLI.py
{"status": "OK", "address": ["600 Broadway #400, Kansas City, MO 64105, USA"]}
{"status": "INCOMPLETE", "address": ["Los Angeles, CA 90001, USA"]}
{"status": "OK", "address": ["1900 South Blvd #304, Charlotte, NC 28203, USA"]}
{"status": "OK", "address": ["4217 Olympus View Dr, Salt Lake City, UT
84124, USA"]}
{"status": "OK", "address": ["1472 Serene Rd, Oceanside, CA 92057, USA"]}
{"status": "INCOMPLETE", "address": ["Colombia"]}
{"status": "OK", "address": ["1647 8th Ave, Brooklyn, NY 11215, USA"]}
....
</pre>

You can also call the checkAdd() function directly, passing it an address as a string.
<pre>
Python 2.7.3 (default, May  9 2012, 23:42:16)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import normCLI
>>> normCLI.checkAdd("1955 Landings Drive CA")
'{"status": "OK", "address": ["1955 Landings Dr, Mountain View, CA
94043, USA"]}'
</pre>