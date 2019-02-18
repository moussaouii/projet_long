from flask import Flask, request, jsonify
from rasa_nlu.model import Interpreter
app = Flask(__name__)

interpreter = Interpreter.load("./models/current/nlu")
@app.route('/api/parse', methods=['GET','POST'])
def hello():
    content = request.json
    message = content["message"]
    token = content["token"]
    user_id = content["user_id"]
    result = interpreter.parse(message)
    return jsonify(result)

@app.route('/hello', methods=['GET','POST'])
def helloworld():
    return jsonify({'test':'it work'})

if __name__ == '__main__':
    app.run(debug=True) 





