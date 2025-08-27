from flask import Flask

app = Flask(__name__)

@app.route('/test1', methods=['GET'])
def test1():
    return 'Test 1'