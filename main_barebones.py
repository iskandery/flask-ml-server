from flask import Flask

app = Flask(__name__)

@app.route('/test_endpoint', methods=['GET'])
def test_function():
    print("I made my own web app!")
    return "I'm tired"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
