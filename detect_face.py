import cv2
import pickle
import face_recognition
import numpy as np
from class_tkinter import Window
import tkinter as tk
import endCoding


cap = None

dem_face_correct =0

def stop():
    global cap
    cap.release()
    cv2.destroyAllWindows()
def face_detect(app):
    with open('EndCoding.p', "rb") as f:
        end_code_with_id = pickle.load(f)
        end_code_know, id = end_code_with_id
    global dem_face_correct

    def update():
        global cap
        global dem_face_correct
        success, img = cap.read()
        if success:
            imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            face_current_frame = face_recognition.face_locations(imgS)
            end_code_current_frame = face_recognition.face_encodings(imgS, face_current_frame)

            for enco_face, face_loc in zip(end_code_current_frame, face_current_frame):
                matches = face_recognition.compare_faces(end_code_know, enco_face)
                face_dis = face_recognition.face_distance(end_code_know, enco_face)
                
                matchIndex = np.argmin(face_dis)
                
                if matches[matchIndex]:
                    dem_face_correct+=1

                    if dem_face_correct==3 :
                        app.is_have_student(id[matchIndex])
                        dem_face_correct=0
                    top, right, bottom, left = face_loc
                    top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
                    cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            app.active_home(img_rgb)
        app.root.after(10, update)
    update()

def run_cap():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(3, 400)
    cap.set(4, 300)

def detect_know_face(root,name):
    run_cap()
    app = Window(root,name)
    face_detect(app)
    app.run()
