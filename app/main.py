from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
    return 'Hello, from the slack bot with python and Flask 1.1.2!'

@app.route('/api/v1/slack/outgoing-webhook', methods=["POST"])
def form_xxx():
    req = request.form
    print(req)
    return jsonify(req)

if __name__ == '__main__':
    app.run(host='0.0.0.0') # port=8080, debug=True
