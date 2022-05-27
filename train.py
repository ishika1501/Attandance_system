from imp import IMP_HOOK
from tkinter import*
from tkinter import ttk
from tkinter.tix import IMAGE
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        title_lbl = Label(self.root, text="TRAIN YOUR DATA SET", font=(
            "Arial", 30, "bold"), bg="#afd9e4", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=75)

        # ------------------------------------------------------------top image-------------------------------------------------------------------
        img_top = Image.open(r"images\imagebottom.jpg")
        img_top = img_top.resize((1530, 320), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=320)

        # --------------------------------------------------------------button---------------------------------------------------------------------
        b1_1 = Button(self.root, text="TO TRAIN DATA CLICK HERE", command=self.train_classifier,
                      cursor="hand2", font=("Arial", 18, "bold"), bg="#026573", fg="white")
        b1_1.place(x=0, y=370, width=1530, height=40)

        # -----------------------------------------------------------bottom image------------------------------------------------------------------
        img_bottom = Image.open(r"images\imagetop.jpg")
        img_bottom = img_bottom.resize((1530, 380), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=410, width=1530, height=380)
# -------------------------------------------------------------------Train data-------------------------------------------------------------------

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image conversion
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
            # cv2.destroyAllWindows()
        ids = np.array(ids)

        # --------------------------------------------------------------Train the classifier and save---------------------------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
