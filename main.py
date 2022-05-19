from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")
        
        #------------------background image-----------------
        img3=Image.open(r"C:\Users\my pc\Desktop\current_project\images\background.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=540)


        #-------------background label-----------------
        title_lbl=Label(bg_img,text="FACE RECOGNISATION ATTANDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #-------------student button------------------
        img4=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)


        #-------------detect face------------------
        img5=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img5=img5.resize((1530,710),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)

         #-------------Attandance face button------------------
        img6=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img6=img6.resize((1530,710),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)


    #------------------------function buttons----------------

    def student_details(self):
           self.new_window=Toplevel(self.root)
           self.app=Student(self.new_window)


















if __name__ == "__main__":
        root=Tk()
        obj=Face_recognition_system(root)
        root.mainloop()
