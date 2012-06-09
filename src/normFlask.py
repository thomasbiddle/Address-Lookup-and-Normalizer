import normCLI
from flask import Flask
from flask import request

app = Flask(__name__)
	
@app.route("/", methods=['POST', 'GET'])
def newTest():
	if request.method == 'POST':
		return normCLI.checkAdd(request.form['input'])
	else:
		return normCLI.checkAdd(request.args.get('input'))
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')