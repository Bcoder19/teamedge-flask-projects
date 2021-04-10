from flask import Flask, request, redirect, render_template, current_app as app
from sense_hat import SenseHat
import sys
import sqlite3

app = Flask(__name__)
sense = SenseHat()


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/success',methods=['POST','GET'])
def success():
    message = request.form.get("message")
    name = request.form.get("name")
    display = message + "Love, " + name

    conn = sqlite3.connect('./static/data/inspirationBoard.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, message) VALUES((?),(?))", (name,message))
    cursor.commit()
    #close databae connection
    conn.close()

    sense.show_message(display, text_colour=[100,41,71])
    return render_template('success.html', message = message)

# @app.route()
# def all():
#     conn = sqlite3.connect('./static/data/inspirationBoard.db')
#     cursor = conn.cursor()
#     messages = []
#     rows  = curs.execute("SELECT * from messages")
#     for row in rows:
#         message = {'name':row[0], 'message':row[1]}
#         messages.append(message)
#     conn.close()







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')