from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def users():
    return jsonify({})


if __name__ == '__main__':
    app.run()