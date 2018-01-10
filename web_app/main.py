from flask import Flask, render_template, request
from thread import start_new_thread

app = Flask(__name__)

CurrentSignal = "White"

@app.route('/', methods=['GET'])

def Main():
	global CurrentSignal

	if request.args.get('Signal'):
		CurrentSignal=request.args.get('Signal')
		print CurrentSignal
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
