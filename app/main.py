from flask import Flask, request, jsonify
from bot import command
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def hello_world():
    command.hello()
    return 'Hello, from the slack bot with python and Flask 1.1.2!'

@app.route('/api/v1/slack/outgoing-webhook', methods=["POST"])
def slackOutgoing():
    outgoing = request.form
    app.logger.info('Teste %s', outgoing['user_name'])
    app.logger.info('Teste %s', outgoing['user_name'])
    # print(outgoing)
    return jsonify(outgoing)

if __name__ == '__main__':
    app.run(host='0.0.0.0') # port=8080, debug=True
