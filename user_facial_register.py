import cv2
import numpy as np
import os
import dlib
from imutils import face_utils
from imutils.face_utils import FaceAligner
from tkinter import *


def make_dataset():
    detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    face_aligner = FaceAligner(shape_predictor, desiredFaceWidth=200)

    cam = cv2.VideoCapture(0)
    name = entryUsername.get()
    root.destroy()
    path = 'images'
    print(path)
    directory = os.path.join(path, name)
    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok='True')

    number_of_images = 0
    count = 0

    while True:
        ret, frame = cam.read()

        frame = cv2.flip(frame, 1)

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(frame_gray)
        if len(faces) == 1:
            face = faces[0]
            (x, y, w, h) = face_utils.rect_to_bb(face)
            face_img = frame_gray[y-50:y + h+100, x-50:x + w+100]
            face_aligned = face_aligner.align(frame, frame_gray, face)

        cv2.imwrite(os.path.join(directory, str(
            name+str(number_of_images)+'.jpg')), face_aligned)
        number_of_images += 1
        cv2.imshow('Video', frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cam.release()
    cv2.destroyAllWindows()

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()

def get_facreg_win():
    global root
    root = Tk()
    root.title("Facial register")
    root.geometry("300x200")
    root.configure(background="black")
    global text
    text = Label(root, text = "Main page", bg = "black", fg = "white")
    text.config(font=("Chiller", 20))
    text.pack()
    Space()
    global entryUsername
    entryUsername = Entry (root) 
    entryUsername.pack()
    Space()
    global buttonorg
    buttonorg= Button(root, text = "Start", command =make_dataset, state = ACTIVE)
    buttonorg.pack()
    Space()
    root.mainloop()
