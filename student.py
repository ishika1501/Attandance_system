from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

         #------------------background image-----------------
        img3=Image.open(r"C:\Users\my pc\Desktop\current_project\images\background.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=1800)


        #-------------background label-----------------
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #------------------left side label frame-------------

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",15,"bold"))
        Left_frame.place(x=20,y=0,width=760,height=750)

        img_left=Image.open(r"C:\Users\my pc\Desktop\current_project\images\rectangle.jpg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=39,y=80,width=750,height=120)

        #-----------------------current course details--------------------
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",15,"bold"))
        current_course_frame.place(x=20,y=135,width=760,height=130)

        #department:

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",10,"bold"),width=13,state="read only")
        dep_combo["values"]=("select Department","computer","mechanical","EIE","civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course:
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",10,"bold"),width=13,state="read only")
        course_combo["values"]=("select Course","computer","mechanical","EIE","civil")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)


        #year:

        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",10,"bold"),width=17,state="read only")
        year_combo["values"]=("select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester:
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",10,"bold"),width=17,state="read only")
        semester_combo["values"]=("select Semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #-----------------------Class student  details--------------------
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=20,y=260,width=760,height=430)

        #studentID:
        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20)
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #studentname:
        studentName_label=Label(class_student_frame,text="Student NAme:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        studentName_label=ttk.Entry(class_student_frame,width=20)
        studentName_label.grid(row=0,column=3,padx=10,sticky=W)

        #studentDivision
        studentName_label=Label(class_student_frame,text="Student Division:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        studentName_label=ttk.Entry(class_student_frame,width=20)
        studentName_label.grid(row=1,column=1,padx=10,sticky=W)

        #roll no:
        rollno_entry=Label(class_student_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="white")
        rollno_entry.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,width=20)
        rollno_entry.grid(row=1,column=3,padx=10,sticky=W)

        #gender:
        gender_entry=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_entry.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20)
        gender_entry.grid(row=2,column=1,padx=10,sticky=W)

        #DOB:
        DOB_entry=Label(class_student_frame,text="dd-mm-yyyy:",font=("times new roman",13,"bold"),bg="white")
        DOB_entry.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20)
        DOB_entry.grid(row=2,column=3,padx=10,sticky=W)

        #email:
        studentemail_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",13,"bold"),bg="white")
        studentemail_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        studentemail_label=ttk.Entry(class_student_frame,width=20)
        studentemail_label.grid(row=3,column=1,padx=10,sticky=W)

        #phonenumber:
        studentph_label=Label(class_student_frame,text="Phone no:",font=("times new roman",13,"bold"),bg="white")
        studentph_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        studentph_label=ttk.Entry(class_student_frame,width=20)
        studentph_label.grid(row=3,column=3,padx=10,sticky=W)

        #address:
        studentaddress_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        studentaddress_label.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        studentaddress_label=ttk.Entry(class_student_frame,width=20)
        studentaddress_label.grid(row=4,column=1,padx=10,sticky=W)

        #teacher name :
        Teachername_label=Label(class_student_frame,text="Teachers name",font=("times new roman",13,"bold"),bg="white")
        Teachername_label.grid(row=4,column=2,padx=2,pady=10,sticky=W)

        Teachername_label=ttk.Entry(class_student_frame,width=20)
        Teachername_label.grid(row=4,column=3,padx=10,sticky=W)

        #-----------radio Button-----------
        radiobtn1=ttk.Radiobutton(class_student_frame,text="take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="no photo sample",value="Yes")
        radiobtn2.grid(row=6,column=1)

        #-----------bbuttons frames-----------
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        takephoto_btn=Button(btn_frame,text="Take a photo",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=1,column=0)

        resetphoto_btn=Button(btn_frame,text="Reset photo",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        resetphoto_btn.grid(row=1,column=1)




        #---------------------------------------Right side label frame---------------------------------------------------------

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",15,"bold"))
        Right_frame.place(x=810,y=0,width=660,height=650)

        img_right=Image.open(r"C:\Users\my pc\Desktop\current_project\images\rectangle.jpg")
        img_right=img_right.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=750,height=120)

        #------------------------------Search system-----------------------------------
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",15,"bold"))
        search_frame.place(x=10,y=120,width=630,height=70)

        search_label=Label(search_frame,text="search:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=-0,column=0,padx=2,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=17,state="read only")
        search_combo["values"]=("select","Roll no","phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=20)
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showall_btn=Button(search_frame,text="Show all",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2)

        #---------------------------table frame----------------------
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=630,height=270)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)





        


        








if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()