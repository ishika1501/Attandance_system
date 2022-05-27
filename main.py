from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import cv2


class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        # ----------------------------------------------------background image-------------------------------------------------------
        img3 = Image.open(r"images\abc2.jpg")
        img3 = img3.resize((1730, 1000), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1700, height=830)

        # -----------------------------------------------------background label-----------------------------------------------------
        title_lbl = Label(bg_img, text="FACE  RECOGNISATION  ATTANDANCE  SYSTEM", font=(
            "Humphrey", 30, "bold"), bg="#afd9e4", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # -----------------------------------------------------Student button-------------------------------------------------------
        img4 = Image.open(r"images\student_details.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=100, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,
                      cursor="hand2", font=("Arial", 15, "bold"), bg="white", fg="grey")
        b1_1.place(x=100, y=350, width=220, height=40)

        # ------------------------------------------------------Detect face---------------------------------------------------------
        img5 = Image.open(r"images\face_detector.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=650, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="Face detector", cursor="hand2", command=self.face_data, font=(
            "Arial", 15, "bold"), bg="white", fg="grey")
        b1_1.place(x=650, y=350, width=220, height=40)

        # ----------------------------------------------------Attendance face button------------------------------------------------
        img6 = Image.open(r"images\attendance.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.attendance_data)
        b1.place(x=100, y=440, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=(
            "Arial", 15, "bold"), bg="white", fg="grey")
        b1_1.place(x=100, y=630, width=220, height=40)

        # -------------------------------------------------------Train data button--------------------------------------------------
        img8 = Image.open(r"images\train_data.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=380, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=(
            "Arial", 15, "bold"), bg="white", fg="grey")
        b1_1.place(x=380, y=350, width=220, height=40)

        # --------------------------------------------------------Photo face button-------------------------------------------------
        img99 = Image.open(r"images\photo.jpg")
        img99 = img99.resize((200, 200), Image.ANTIALIAS)
        self.photoimg99 = ImageTk.PhotoImage(img99)

        b1 = Button(bg_img, image=self.photoimg99,
                    cursor="hand2", command=self.open_img)
        b1.place(x=380, y=440, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Photo", cursor="hand2", command=self.open_img, font=(
            "Arial", 15, "bold"), bg="white", fg="grey")
        b1_1.place(x=380, y=630, width=220, height=40)

        # ------------------------------------------------------About Developer button----------------------------------------------
        # img10=Image.open(r"images\developer.jpg")
        # img10=img10.resize((200,200),Image.ANTIALIAS)
        # self.photoimg9=ImageTk.PhotoImage(img10)

        # b1=Button(bg_img,image=self.photoimg9)
        # b1.place(x=950,y=380,width=220,height=220)

        # b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="grey")
        # b1_1.place(x=950,y=580,width=220,height=40)

    # --------------------------------------------------------------------Image opening---------------------------------------------------
    def open_img(self):
        os.startfile("data")

    # --------------------------------------------------------------------function buttons------------------------------------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
