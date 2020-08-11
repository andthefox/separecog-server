# api.py
# -*- coding: utf-8 -*-

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import cv2
# from mtcnn import MTCNN

# detector = MTCNN()

app = FastAPI()


@app.post("/")
def send_result():
    return {'hello': 'world'}
