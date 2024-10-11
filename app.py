from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/al/admin/agents', methods=['GET'])
def get_data():
    # Sample JSON response
    data = {
        'message': 'Hello, World!',
        'status': 'success',
        'data': [
            {
              'active': 'true',
              'config_uuid': '1234567890',
              'created_at': '2024-01-01T00:00:00.000Z',
              'end_at': '2024-01-01T00:00:00.000Z',
              'name': 'Fleet 1',
              'project_id': '1234567890',
              'updated_at': '2024-01-01T00:00:00.000Z',
              'uuid': '1234567890',
              'user_uuid': '1234567890'
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)