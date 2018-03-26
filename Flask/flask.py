# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
    # return 'Hello comment sa vas!'


	
from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)
   
if __name__ == '__main__':
    app.run()