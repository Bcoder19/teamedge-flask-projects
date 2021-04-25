from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat
from flask_apscheduler import APScheduler
import sqlite3

app = Flask(__name__)
sense = SenseHat()




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
