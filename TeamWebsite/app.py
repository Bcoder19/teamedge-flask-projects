from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/Brios")
def Brios():
	return render_template('Brios.html')


@app.route("/Clay")
def Clay():
	return render_template('Clay.html')


@app.route("/Lateef")
def Lateef():
	return render_template('Lateef.html')


@app.route("/Rachel")
def Rachel():
	return render_template('Rachel.html')

if __name__ == '__main__':
	app.run(debug =True, host = "0.0.0.0")
