from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')



if __name__ == '__main__':
  app.run(debug=True)
 


