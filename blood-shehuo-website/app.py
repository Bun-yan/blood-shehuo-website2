from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'msg': '用户名和密码不能为空'})
    if username in users:
        return jsonify({'success': False, 'msg': '用户名已存在'})
    users[username] = password
    return jsonify({'success': True, 'msg': '注册成功'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        session['user'] = username
        return jsonify({'success': True, 'msg': '登录成功'})
    return jsonify({'success': False, 'msg': '用户名或密码错误'})

if __name__ == '__main__':
    app.run(debug=True)