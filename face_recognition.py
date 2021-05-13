import cv2
import numpy as np
import pandas as pd

def face_recognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Trainer/trainer.yml')
    cascPathface = "haarcascade_frontalface_alt2.xml" # USING PREDEFINED FILE
    faceCascade = cv2.CascadeClassifier(cascPathface)

    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0
    df1 = pd.read_excel("Data_of_Employees.xlsx", engine='openpyxl')
    names = ['None'] + df1['Name'].tolist()

    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # TURNING VIDEO ON
    blank = np.zeros((500, 1000, 3), dtype=np.uint8)  # CREATING A BLANK IMAGE TO DISPLAY THE ERROR MESSAGE
    video_capture.set(3, 640)  # set video widht
    video_capture.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * video_capture.get(3)
    minH = 0.1 * video_capture.get(4)

    while video_capture.isOpened():

        ret, frame = video_capture.read()
        # IF CONDITION TO CHECK PROPER WORKING
        if not ret:
            print("Unable to open video")
            break
        frame = cv2.flip(frame, 1)  # FLIPPING IT VERTICALLY
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # CONVERTING INTO GRAY SCALE
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)),
                                             flags=cv2.CASCADE_SCALE_IMAGE)
        # IF MORE THAN 1 FACE IS DETECTED THEN STOP
        if len(faces) > 1:
            cv2.destroyWindow('Video')
            cv2.putText(blank, "'Sorry' Stopped due to more faces", (0, 50), None, 1, (255, 255, 255), 2)
            cv2.imshow('Error! Closed', blank)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # CREATING RECTANGLE AROUND FACE
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # PREDICTING USING TRAINED MODEL
            # If confidence is less them 100 ==> "0" : perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                cv2.putText(frame, "Face Matched with the person", (50, 50), font, 1, (255, 255, 255), 2)
                #print("Face Matched with",id,",Door Opened")
            else:
                id = "Unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                #cv2.putText(frame, "For Emergency SOS, Press 's'", (50, 50), font, 1, (255, 255, 255), 2)
                # ADD SOS FUNCTION

            cv2.putText(frame, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)  # Displaying text "NAME"
            cv2.putText(frame, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0),1)  # Displaying text "CONFIDENCE"

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_recognition()

