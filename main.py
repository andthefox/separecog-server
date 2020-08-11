# main.py
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import tensorflow as tf
from mtcnn import MTCNN
from flask import Flask, request, jsonify

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)


detector = MTCNN()

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route("/imageprocess", methods=['POST'])
def send_result():
    nparr = np.fromstring(request.data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = detector.detect_faces(img_np)
    # print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=80)
