from flask import Flask, render_template
app = Flask(__name__)


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


if __name__ == '__main__':
  app.run(debug=True)
 


