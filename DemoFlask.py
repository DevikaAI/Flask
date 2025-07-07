from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🔢 Welcome to the Math API! Use /add, /subtract, /multiply, /divide endpoints."

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(result=a / b)

#if __name__ == '__main__':
   # app.run(debug=True)
