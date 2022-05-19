from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        #-------------------Variables-------------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=13,state="read only")
        dep_combo["values"]=("select Department","computer","mechanical","EIE","civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course:
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=13,state="read only")
        course_combo["values"]=("select Course","computer","mechanical","EIE","civil")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)


        #year:

        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=17,state="read only")
        year_combo["values"]=("select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester:
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=17,state="read only")
        semester_combo["values"]=("select Semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #-----------------------Class student  details--------------------
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=20,y=260,width=760,height=430)

        #studentID:
        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20)
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #studentname:
        studentName_label=Label(class_student_frame,text="Student NAme:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        studentName_label=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20)
        studentName_label.grid(row=0,column=3,padx=10,sticky=W)

        #studentDivision
        studentName_label=Label(class_student_frame,text="Student Division:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        studentName_label=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20)
        studentName_label.grid(row=1,column=1,padx=10,sticky=W)

        #roll no:
        rollno_entry=Label(class_student_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="white")
        rollno_entry.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20)
        rollno_entry.grid(row=1,column=3,padx=10,sticky=W)

        #gender:
        gender_entry=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_entry.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20)
        #gender_entry.grid(row=2,column=1,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17,state="read only")
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #DOB:
        DOB_entry=Label(class_student_frame,text="dd-mm-yyyy:",font=("times new roman",13,"bold"),bg="white")
        DOB_entry.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20)
        DOB_entry.grid(row=2,column=3,padx=10,sticky=W)

        #email:
        studentemail_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",13,"bold"),bg="white")
        studentemail_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        studentemail_label=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20)
        studentemail_label.grid(row=3,column=1,padx=10,sticky=W)

        #phonenumber:
        studentph_label=Label(class_student_frame,text="Phone no:",font=("times new roman",13,"bold"),bg="white")
        studentph_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        studentph_label=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20)
        studentph_label.grid(row=3,column=3,padx=10,sticky=W)

        #address:
        studentaddress_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        studentaddress_label.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        studentaddress_label=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20)
        studentaddress_label.grid(row=4,column=1,padx=10,sticky=W)

        #teacher name :
        Teachername_label=Label(class_student_frame,text="Teachers name",font=("times new roman",13,"bold"),bg="white")
        Teachername_label.grid(row=4,column=2,padx=2,pady=10,sticky=W)

        Teachername_label=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20)
        Teachername_label.grid(row=4,column=3,padx=10,sticky=W)

        #-------------------------------------radio Button-----------------------------------------------------
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #---------------------------------------------bbuttons frames-----------------------------------------------------
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
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

        #-------------------------------------------------Search system--------------------------------------------------------
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
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #----------------------------Function Declartion ---------------------------------

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error all fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ishikaraj@123",database="database1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",  (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()

                                                                                                            ))  
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)                                                                                           
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)},parent=self.root")


    #----------------------------------------fetch data--------------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ishikaraj@123",database="database1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    #--------------------  get cursor---------------- 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #----------------------------DATA update------------------------    

    def update_data(self)
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
           messagebox.showerror("Error all fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ishikaraj@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(  
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data() 
                conn.close()       
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #--------------------------DELETE FUNCTION-------------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ishikaraj@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:    
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   



   #----------------------------reset data ------------------------------
   def reset_data(self): 
       self.var_dep.set("Select Department")
       self.var_course.set("Select course")
       self.var_year.set("Select year")
       self.var_semester.set("Select semester")
       self.var_std_id("")
       self.var_std_name("")
       self.var_div.set("")
       self.var_roll.set(""),
       self.var_gender.set("Male"),
       self.var_dob.set(""),
       self.var_email.set(""),
       self.var_phone.set(""),
       self.var_address.set(""),
       self.var_teacher.set(""),
       self.var_radio1.set("")







if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()