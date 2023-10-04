from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def language ():
  a = request.args
  if a == {}:
    return 'There is nothing here'
  elif a['lang'] == 'english':
    return 'Hello, good morning'
  elif a['lang'] == 'french':
    return 'Bonjour, bonjour'
  elif a['lang'] == 'hindi':
    return 'hailo suprabhaat'

@app.route('/')
def home():
  return 'Welcome to flask'

app.run(host='0.0.0.0', port=81)