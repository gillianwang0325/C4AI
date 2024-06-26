from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Avanade Health App!"

@app.route('/predict', methods=['POST'])
def predict():
    # Implement your image classification logic here
    return jsonify({"prediction": "This is a placeholder response."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
