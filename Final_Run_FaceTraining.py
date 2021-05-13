import cv2
import os
import numpy as np
from PIL import Image


def face_training():
    cascPathface = "haarcascade_frontalface_alt2.xml" # USING PREDEFINED FILE
    detector = cv2.CascadeClassifier(cascPathface)

    path = 'Dataset_Faces'  # PATH TO THE STORED FACE SAMPLES
    facesamples = []  # STORING FACE SAMPLES
    ids = []  # STORING FACE ID'S
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]  # STORING IMAGE PATH IN ARRAY
    # ITERATING THROUGH IMAGE PATH
    for imagepath in imagepaths:

        img_PIL = Image.open(imagepath).convert('L')  # CONVERT TO GRAY SCALE
        img_numpy = np.array(img_PIL, 'uint8')  # CONVERT TO NUMPY ARRAY
        Id = int(os.path.split(imagepath)[-1].split(".")[1])  # TAKING ONLY ID NUMBERS
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            facesamples.append(img_numpy[y:y + h, x:x + w])  # APPENDING FACES
            ids.append(Id)  # APPENDING ID'S

    # noinspection PyUnresolvedReferences
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # RECOGNIZER OBJECT CREATION
    recognizer.train(facesamples, np.array(ids))  # TRAINING FACE SAMPLES AND ID'S
    recognizer.write('Trainer/trainer.yml')  # CREATING A .yml FILE WITH TRAINED DATA

if __name__ == '__main__':
    face_training()




