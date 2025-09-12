from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/recommend')
def recommend():
    # 占位实现
    return jsonify({ 'recommendations': [
        {'id': 1, 'title': 'Python 入门', 'score': 0.9},
        {'id': 2, 'title': 'Linux 基础', 'score': 0.8}
    ]})

if __name__ == '__main__':
    app.run(port=5001)
