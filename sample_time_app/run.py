from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'
    
@app.route('/time')
def get_current_time():
    # Function to return the current time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
