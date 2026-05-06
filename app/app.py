from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "ok",
        "env": "production"
        }), 200

@app.route('/healthz', methods=['GET'])
def healthz():
           return jsonify({
                "healthy": True
        }), 200
@app.route('/readyz', methods=['GET'])
def readyz():
           return jsonify({
                "ready": True
        }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)