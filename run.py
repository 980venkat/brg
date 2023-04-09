import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # This is the magic

APP = Flask(__name__)  # Standard Flask app
CORS(APP)

@APP.route('/', methods=['POST']) 
def login():
    login_data={"status":"fail"}
    data = request.json
    print(data)
    print(data['email'])
    print(data['passwd'])

    login_data={"status":"success"}

    return jsonify(login_data)

@APP.route('/remediate', methods=['POST']) 
def remediate():
    data = request.json
    print(data)
    return jsonify(data)

@APP.route('/changepwd', methods=['POST']) 
def changepwd():
    data = request.json
    print(data)
    return jsonify(data)
    
if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
  