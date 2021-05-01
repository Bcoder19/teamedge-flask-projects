from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat
from flask_apscheduler import APScheduler
import sqlite3

app = Flask(__name__)
sense = SenseHat()

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def createTask():
    #Retrieving task data from HTML form
    description = request.form.get('description')
    datetime = request.form.get('datetime')

    #Store task data in sqlite3 db
    conn = sqlite3.connect('./static/data/mytasks.db')
    curs = conn.cursor()
    curs.execute("insert into mytasks (description, datetime) values((?),(?))",(description,datetime))
    conn.commit()
    conn.close()
    render_template('index.html',description = description, datetime = datetime)

    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
