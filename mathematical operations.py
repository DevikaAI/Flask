from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/math', methods=['POST'])
def calculate():
    data = request.get_json()

    operation = data.get("operation")
    num1 = data.get("num1")
    num2 = data.get("num2")

    if not all([operation, isinstance(num1, (int, float)), isinstance(num2, (int, float))]):
        return jsonify({"error": "Invalid input. Provide 'operation', 'num1' and 'num2'."}), 400

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Division by zero not allowed."}), 400
            result = num1 / num2
        else:
            return jsonify({"error": f"Unsupported operation '{operation}'."}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

    return jsonify({
        "operation": operation,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
