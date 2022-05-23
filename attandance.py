from asyncore import write
from lib2to3.pgen2.token import NEWLINE
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox

from colorama import Cursor
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]

class Attandance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face recognisation system")

                #variables:
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()


                #first image
                img=Image.open(r"images\abc.jpeg")
                img=img.resize((1500,800),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=1500,height=100)

                #second image :
                img=Image.open(r"images\abc.jpeg")
                img=img.resize((1500,1500),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=800,y=0,width=1500,height=200)

                #background image:
                img3=Image.open(r"images\abc.jpeg")
                img3=img3.resize((1500,1300),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=0,width=1530,height=1800)


                title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("Arial",25,"bold"),bg="white",fg="grey")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=10,y=55,width=1500,height=600)
                #left frame:
                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Attendance details",font=("Arial",15,"bold"))
                Left_frame.place(x=20,y=0,width=760,height=780)

                img_left=Image.open(r"images\abc.jpeg")
                img_left=img_left.resize((1500,1300),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=0,y=3,width=850,height=120)

                left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=6,y=135,width=740,height=600)

                #-----------------------------labels and entry---------------------------------------:

                #attendance id:
                attendanceId_label=Label(left_inside_frame,text="Attendance ID: ",font=("Arial",13,"bold"),bg="white")
                attendanceId_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

                attendanceId_entry=ttk.Entry(left_inside_frame,width=20)
                attendanceId_entry.grid(row=0,column=1,padx=10,sticky=W)


                #roll
                rollLabel_label=Label(left_inside_frame,textvariable=self.var_atten_id,text="Roll: ",font=("Arial",13,"bold"),bg="white")
                rollLabel_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

                atten_roll=ttk.Entry(left_inside_frame,width=20)
                atten_roll.grid(row=0,column=3,padx=8)

                #name:
                rollLabel_label=Label(left_inside_frame,textvariable=self.var_atten_name,text="Name: ",font=("Arial",13,"bold"),bg="white")
                rollLabel_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

                atten_roll=ttk.Entry(left_inside_frame,width=20)
                atten_roll.grid(row=1,column=1,padx=8)

                #departemnt:
                depLabel_label=Label(left_inside_frame,textvariable=self.var_atten_dep,text="Department: ",font=("Arial",13,"bold"),bg="white")
                depLabel_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

                atten_dep=ttk.Entry(left_inside_frame,width=20)
                atten_dep.grid(row=1,column=3,padx=8)

                #time:
                timeLabel_label=Label(left_inside_frame,textvariable=self.var_atten_time,text="Time: ",font=("Arial",13,"bold"),bg="white")
                timeLabel_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

                atten_time=ttk.Entry(left_inside_frame,width=20)
                atten_time.grid(row=2,column=1,padx=8)

                #date:
                dateLabel_label=Label(left_inside_frame,textvariable=self.var_atten_date,text="Date: ",font=("Arial",13,"bold"),bg="white")
                dateLabel_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

                atten_date=ttk.Entry(left_inside_frame,width=20)
                atten_date.grid(row=2,column=3,padx=8)

                #attendance:
                atten_status=Label(left_inside_frame,textvariable=self.var_atten_attendance,text="Attendance: ",font=("Arial",13,"bold"),bg="white")
                atten_status.grid(row=3,column=0,padx=2,pady=10,sticky=W)

                self.atten_status=ttk.Combobox(left_inside_frame,font=("Arial",10,"bold"),width=17,state="read only")
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)
                self.atten_status.current(0)

                #--------------------------buttons------------------------------

                btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=6,y=370,width=715,height=35)

                save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("Arial",13,"bold"),bg="blue",fg="white")
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("Arial",13,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Update",width=17,font=("Arial",13,"bold"),bg="blue",fg="white")
                delete_btn.grid(row=0,column=2)

                reset_btn=Button(btn_frame,text="Reset",width=17,font=("Arial",13,"bold"),bg="blue",fg="white")
                reset_btn.grid(row=0,column=3)




                #-----------------------right frame----------------------
                Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font=("Arial",15,"bold"))
                Right_frame.place(x=810,y=10,width=640,height=550)

                table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=10,width=600,height=445)

                #--------------------------scroll bar and table-----------------------
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttandanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.AttandanceReportTable.xview)
                scroll_y.config(command=self.AttandanceReportTable.yview)

                self.AttandanceReportTable.heading("id",text="Attendance ID")
                self.AttandanceReportTable.heading("roll",text="Roll")
                self.AttandanceReportTable.heading("name",text="Name")
                self.AttandanceReportTable.heading("department",text="Department")
                self.AttandanceReportTable.heading("time",text="Time")
                self.AttandanceReportTable.heading("date",text="Date")
                self.AttandanceReportTable.heading("attendance",text="Attendance")

                self.AttandanceReportTable["show"]="headings"

                self.AttandanceReportTable.column("id",width=100)
                self.AttandanceReportTable.column("roll",width=100)
                self.AttandanceReportTable.column("name",width=100)
                self.AttandanceReportTable.column("department",width=100)
                self.AttandanceReportTable.column("time",width=100)
                self.AttandanceReportTable.column("date",width=100)
                self.AttandanceReportTable.column("attendance",width=100)


        

                self.AttandanceReportTable.pack(fill=BOTH,expand=1)


        #---------------------fetch data---------------------

        def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReporttable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,Values=i)
        #------------import csv-----------
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)  
        #------------export csv-------------
        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Date","No data found to export",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv*"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfiles,delimiter=",")
                    for i in mydata:
                            exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"succesfully")  
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)             

        #def get_cursor(self):
            



if __name__ == "__main__":
        root=Tk()
        obj=Attandance(root)
        root.mainloop()
