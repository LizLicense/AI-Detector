from flask import Flask, request
from server.detector import OpenaiDetector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/v1/hello')
def detect():
    return "response"


@app.route('/v1/detect', methods=['POST'])
@cross_origin()
def detect_sentence():
    print("enter sentence")

    sentence = request.form['sentence']
    print(sentence)
    detector = OpenaiDetector()
    response = detector.detect(f"{sentence}")
    print(response)
    return response


if __name__ == '__main__':
    app.run()
