from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # 返回前端页面

# 监听客户端连接
@socketio.on('connect')
def handle_connect():
    # 模拟生成的文本数组
    text_array = [
        "这是第一段文字。",
        "这是第二段文字。",
        "这是第三段文字。"
    ]
    
    # 延时逐段发送
    for text in text_array:  
        emit('new_message', text)  # 向前端发送数据
        socketio.sleep(1)

if __name__ == '__main__':
    socketio.run(app, port=5000)
