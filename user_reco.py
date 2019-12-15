# MAI JOACA-TE CU VALORIILE PANA LA SF HACKATHON ULUI  + PICKLE DB
import cv2
import numpy as np
import glob
from scipy.spatial import distance
from imutils import face_utils
from keras.models import load_model
import tensorflow as tf

from utils import *
from inception_blocks_v2 import *

def get_id(string):
    return ''.join([i for i in string if not i.isdigit()])
def get_face():
    FR_model = load_model('nn4.small2.v1.h5')

    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

    threshold = 0.25 # ASTA

    face_database = {}

    print("Getting database")

    for name in os.listdir('images'):
        for image in os.listdir(os.path.join('images',name)):
            identity = os.path.splitext(os.path.basename(image))[0]
            face_database[identity] = utils.img_path_to_encoding(os.path.join('images',name,image), FR_model)

    print("Done")
    cam = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)

        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = frame[y:y+h, x:x+w]
            encoding = img_to_encoding(roi, FR_model)
            min_dist = 100
            identity = None

            for(name, encoded_image_name) in face_database.items():
                dist = np.linalg.norm(encoding - encoded_image_name)
                if(dist < min_dist):
                    min_dist = dist
                    identity = name
            if min_dist < 0.1: #ASTA
                user = get_id(identity[:-1])
                cv2.putText(frame, user, (x, y - 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)
                cam.release()
                cv2.destroyAllWindows()
                return user
            else:
                cv2.putText(frame, 'No matching faces', (x, y - 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255, 0), 2)

        cv2.imshow('Cam', frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cam.release()
    cv2.destroyAllWindows()
