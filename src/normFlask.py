import normCLI
from flask import Flask
from flask import request

app = Flask(__name__)
	
@app.route("/", methods=['POST', 'GET'])
def newTest():
	if request.method == 'POST':
		newAddress = normCLI.checkAdd(request.form['input'])
		return newAddress.jsonAdd()
	else:
		newAddress = normCLI.checkAdd(request.args.get('input'))
		return newAddress.jsonAdd()
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
