Address-Lookup-and-Normalizer
=============================

Given input, works with Google Maps API to return back whether the address is valid or not.

<h3>Examples:</h3>
<br><br>
<pre>
root@Python:~/PythonScripts/AddressNorm# curl localhost:5000 -X POST
-d 'input="1955 Landings Drive CA"'
{"status": "OK", "address": ["1955 Landings Dr, Mountain View, CA 94043, USA"]}
</pre>
<br><br>
<pre>
http://localhost:5000/?input=%221955%20landings%20drive%22
</pre>
<br><br>
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
<br><br>
<pre>
Python 2.7.3 (default, May  9 2012, 23:42:16)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import normCLI
>>> normCLI.checkAdd("1955 Landings Drive CA")
'{"status": "OK", "address": ["1955 Landings Dr, Mountain View, CA
94043, USA"]}'
</pre>