import cv2 
from flask import Flask 
app = Flask(__name__)
camera = cv2.VideoCapture(0)