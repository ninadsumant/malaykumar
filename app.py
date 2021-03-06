from flask import Flask, render_template, Request
from flask_mail import Mail, Message
import os
app = Flask(__name__)


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": '',
    "MAIL_PASSWORD": ''
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/executive')
def executive():
    return render_template('executiveCoaching.html')

@app.route('/mentalstrength')
def mentalstrength():
    return render_template('mentalstrength.html')

@app.route('/meditate')
def meditate():
    return render_template('meditation.html')

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/analyser')
def analyser():
    return render_template('analyser.html')

@app.route('/coachingInto')
def coachingInto():
    return render_template('intro.html')

@app.route('/result', methods=["GET","POST"])
def result():
    return render_template('result.html')



if __name__ == '__main__':
  app.run(debug=False)
 


