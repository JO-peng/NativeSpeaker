from flask import Flask, request,jsonify, send_from_directory
import base64

app = Flask(__name__)



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def home():
    return send_from_directory('static', '简单前端对接.html')

@app.route("/submit", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        text = request.form.get('text', '')
        image = request.files.get('image')
        audio = request.files.get('file')

        print(type(audio))
        print(f"Received text: {text}")
        print(type(text))
        print(f"Received image: {image}")

        # 将图片文件转换为Base64编码的字符串
        image_base64 = base64.b64encode(image.read()).decode('utf-8')
    
        # 将音频文件转换为Base64编码的字符串
        #audio_base64 = base64.b64encode(audio.read()).decode('utf-8')

        print(type(image_base64))
        print(len(image_base64))
        
        # 返回JSON格式的数据，包含图片Base64编码的字符串
        return jsonify({
            'text': text,
            'image': 'data:image/jpeg;base64,' + image_base64,

        })

if __name__ == '__main__':
    app.run(debug=True)

