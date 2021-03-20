from flask import Flask, request, redirect, render_template, current_app as app
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/success',methods=['POST','GET'])
def success():
    message = request.form.get("message")
    sense.show_message(message)
    return render_template('success.html', message = message)







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')