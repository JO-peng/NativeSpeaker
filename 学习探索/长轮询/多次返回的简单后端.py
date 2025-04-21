from flask import Flask, request,jsonify
import time

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

mytext = []

@app.route("/sub-liltest", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        
        text = request.form.get('text', '')
        mytext.append(text)  # 将文本添加到队数组中
        return jsonify({'status': 'Text received'}), 200
        
@app.route('/get-liltest', methods=['GET'])
def get_substring():
    if mytext:
        return jsonify({'text': mytext[0]}), 200
    else:
        # 如果没有，就等一会
        time.sleep(5)
        return jsonify({'text': None}), 204

if __name__ == '__main__':
    app.run(debug=True)

