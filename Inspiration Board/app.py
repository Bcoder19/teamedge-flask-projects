from flask import Flask, request, redirect, render_template, current_app as app
from sense_emu import SenseHat

app = Flask(__name__)
sense = SenseHat()


@app.route('/',methods=['POST','GET'])
def index():

    if request.method == 'POST':
       

        message = request.form.get("message")
        sense.show_message(message)
        
        return redirect('/success')

    return render_template('index.html')


@app.route('/success',methods=['GET'])
def success():
    return render_template('success.html')







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')