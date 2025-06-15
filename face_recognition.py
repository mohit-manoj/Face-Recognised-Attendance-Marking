from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import cv2.face
import face_recognition

class Face_Recognition1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition")

        # Load the trained model
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.isfile("classifier.xml"):
            self.train_classifier()
        self.clf.read("classifier.xml")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("candara", 35), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_1 = Button(self.root, text="DETECT FACE", cursor="hand2", command=self.face_recog,
                      font=("candara", 15), bg="darkblue", fg="white")
        b1_1.place(x=649, y=400, width=220, height=40)

        self.name_list = []


    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # grayscale img
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        # train the classifier and save
        self.clf.train(faces, ids)
        self.clf.write("classifier.xml")

    def recognize(self, img, faceCascade):
        if not hasattr(self, 'clf') or self.clf is None:
            messagebox.showerror("Error", "Eigenfaces model is not trained. Train the model first.")
            return img

        coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face")
        return img
    # attendance doub:name list,variables
    def mark_attendance(self, i, r, n, d):
        with open("kiran.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.split(",")
                self.name_list.append(entry[0])

            if (i not in self.name_list) and (r not in self.name_list) and (n not in self.name_list) and (
                    r not in self.name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Preset")

    def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text):
        if not hasattr(self, 'clf') or self.clf is None:
            return []

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []  # Initialize coord as an empty list

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = self.clf.predict(gray_image[y:y + h, x:x + w])  # Replaced clf with self.clf
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc",
                                           database="face_recognition")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT name FROM student WHERE id =" + str(id))
            name_result = my_cursor.fetchone()
            if name_result:
                n = str(name_result[0])

                if isinstance(n, str):
                    n = [n]

                n = "+".join(map(str, n))
            else:
                n = "Unknown"

            my_cursor.execute("SELECT RollNo FROM student WHERE id = " + str(id))
            roll_result = my_cursor.fetchone()

            if roll_result and len(roll_result) > 0:
                r = str(roll_result[0])

                if isinstance(r, str):
                    r = [r]

                r = "+".join(map(str, r))
            else:
                r = "Unknown"

            my_cursor.execute("SELECT department FROM student WHERE id = " + str(id))
            department_result = my_cursor.fetchone()

            if department_result and len(department_result) > 0:
                d = str(department_result[0])

                if isinstance(d, str):
                    d = [d]

                d = "+".join(map(str, d))
            else:
                d = "Unknown"

            my_cursor.execute("SELECT id FROM student WHERE id = " + str(id))
            id_result = my_cursor.fetchone()

            if id_result and len(id_result) > 0:
                i = str(id_result[0])

                if isinstance(i, str):
                    i = [i]

                i = "+".join(map(str, i))
            else:
                i = "Unknown"

            if confidence >77:
                print(confidence)
                cv2.putText(img, f"id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"RollNo:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                if isinstance(n, str):
                    n = [n]
                n = "+".join(map(str, n))
                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendance(i, r, n, d)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            coord.append([x, y, w, h])  # Append values to coord list

        return coord

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)

            if cv2.waitKey(10) == 13:
                break
            if cv2.getWindowProperty("Welcome TO face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition1(root)
    root.mainloop()