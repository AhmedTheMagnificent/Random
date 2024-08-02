import tensorflow as tf
import cv2 as cv
import mediapipe as mp
import numpy as np

mpHolistic = mp.solutions.holistic
mpDrawing = mp.solutions.drawing_utils

def mediapipeDetection(image, model):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    image.flags.writeable = True
    return image, results

def drawLandmarks(image, results):
    mpDrawing.draw_landmarks(image, results.right_hand_landmarks, mpHolistic.HAND_CONNECTIONS)
    mpDrawing.draw_landmarks(image, results.right_hand_landmarks, mpHolistic.HAND_CONNECTIONS)
    mpDrawing.draw_landmarks(image, results.face_landmarks, mpHolistic.FACEMESH_CONTOURS)
    
cap = cv.VideoCapture(0)
with mpHolistic.Holistic() as model:
    while cap.isOpened():
        ret, frame = cap.read()
        image, results = mediapipeDetection(frame, model)
        drawLandmarks(image, results)
        cv.imshow("Landmarks", image)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
