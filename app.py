from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fleets', methods=['GET'])
def get_data():
    # Sample JSON response
    data = {
        'message': 'Hello, World!',
        'status': 'success',
        'data': [
            {
              'username': 'quandc'
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')