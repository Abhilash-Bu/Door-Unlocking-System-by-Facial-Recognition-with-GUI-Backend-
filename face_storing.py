import cv2
import numpy as np

def face_storing(emp_id): # SENDING EMPLOYEE ID

    cascPathface = "haarcascade_frontalface_alt2.xml" # USING PREDEFINED FILE
    faceCascade = cv2.CascadeClassifier(cascPathface) # CREATING AN OBJECT FOR FACE DETECTION

    count = 0  # TO COUNT THE NUMBER OF IMAGES FOR STORING
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # TURNING ON THE CAMERA
    blank = np.zeros((500, 1000, 3), dtype=np.uint8)  # CREATING A BLANK IMAGE TO DISPLAY THE ERROR MESSAGE
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        # IF LOOP IS USED FOR SAFETY
        if not ret:
            print("Unable to open video")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # CONVERTING FROM NORMAL TO GRAY SCALE
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                             minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)
        frame = cv2.flip(frame, 1)  # FLIPPING THE IMAGE
        # FACE DETECTION AND STORING
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1
            cv2.imwrite(r'Dataset_Faces\User.' + str(emp_id) + '.' +
                        str(count) + ".jpg", gray[y:y + h, x:x + w])

        # IF MORE THAN 2 FACES ARE DETECTED CLOSE THE APPLICATION
        if len(faces) >= 2:
            cv2.destroyWindow('Video')
            # DISPLAYING A BLANK NOTE
            cv2.putText(blank, "Closed! More than 1 face Detected, Restart Again", (0, 50), None, 1, (255, 255, 255), 2)
            cv2.imshow('Note', blank)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

        cv2.imshow("Video", frame)
        cv2.waitKey(250)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break

        if count >= 30: # LIMIT OF 30 PHOTOS
            cv2.destroyWindow('Video')
            # DISPLAYING A BLANK NOTE
            cv2.putText(blank, "Enough face Images recorded", (0, 50), None, 1, (255, 255, 255), 2)
            cv2.imshow('Note', blank)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    emp_id = int(input("Enter your Employee ID\n"))
    face_storing(emp_id)