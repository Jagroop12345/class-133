from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def info():
    return 'this is the areospace website'


@app.route('/aerospace')
def rocket():
    return 'Artemis'

@app.route('/NASA')
def nasa():
    ac = 'Air Canada'
    return render_template('index.html',airline=ac)

app.run(debug=True)
