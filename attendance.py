from asyncore import write
from lib2to3.pgen2.token import NEWLINE
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from colorama import Cursor
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        # ---------------------------------------------------------------variables----------------------------------------------------------------
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ----------------------------------------------------------background image-------------------------------------------------------------
        img3 = Image.open(r"images\abc.jpeg")
        img3 = img3.resize((1530, 1300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=1300)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "Arial", 25, "bold"), bg="#afd9e4", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=650)

        # --------------------------------------------------------------left frame----------------------------------------------------------------
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text=" Student Attendance details", font=("Arial", 15, "bold"))
        Left_frame.place(x=20, y=0, width=760, height=600)

        img_left = Image.open(r"images\banner.jpg")
        img_left = img_left.resize((730, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=3, width=730, height=100)

        # -----------------------------------------------------------labels and entry-------------------------------------------------------------

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=7, y=135, width=740, height=430)

        # attendance id:
        attendanceId_label = Label(left_inside_frame, text="Attendance ID: ", font=(
            "Arial", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_id, width=20)
        attendanceId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # roll
        rollLabel_label = Label(left_inside_frame, text="Roll: ", font=(
            "Arial", 13, "bold"), bg="white")
        rollLabel_label.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        atten_roll = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_roll, width=20)
        atten_roll.grid(row=0, column=3, padx=8)

        # name:
        rollLabel_label = Label(left_inside_frame, text="Name: ", font=(
            "Arial", 13, "bold"), bg="white")
        rollLabel_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        atten_roll = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_name, width=20)
        atten_roll.grid(row=1, column=1, padx=8)

        # departemnt:

        depLabel_label = Label(left_inside_frame, text="Department: ", font=(
            "Arial", 13, "bold"), bg="white")
        depLabel_label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        atten_dep = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_dep, width=20)
        atten_dep.grid(row=1, column=3, padx=8)

        # time:
        timeLabel_label = Label(left_inside_frame, text="Time: ", font=(
            "Arial", 13, "bold"), bg="white")
        timeLabel_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        atten_time = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_time, width=20)
        atten_time.grid(row=2, column=1, padx=8)

        # date:
        dateLabel_label = Label(left_inside_frame, text="Date: ", font=(
            "Arial", 13, "bold"), bg="white")
        dateLabel_label.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        atten_date = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_date, width=20)
        atten_date.grid(row=2, column=3, padx=8)

        # attendance:
        atten_status = Label(left_inside_frame, text="Attendance: ", font=(
            "Arial", 13, "bold"), bg="white")
        atten_status.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=(
            "Arial", 10, "bold"), width=17, state="read only")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=2, pady=10, sticky=W)
        self.atten_status.current(0)

        # --------------------------------------------------------------buttons--------------------------------------------------------------------

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=80, y=350, width=534, height=35)

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=(
            "Arial", 13, "bold"), bg="#afd9e4", fg="white")
        save_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=(
            "Arial", 13, "bold"), bg="#afd9e4", fg="white")
        export_btn.grid(row=0, column=1)

        # update_btn=Button(btn_frame,text="Update",width=17,font=("Arial",13,"bold"),bg="#afd9e4",fg="white")
        # update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=16, font=(
            "Arial", 13, "bold"), bg="#afd9e4", fg="white")
        reset_btn.grid(row=0, column=3)

        # ------------------------------------------------------------Right frame----------------------------------------------------------------
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance details", font=("Arial", 15, "bold"))
        Right_frame.place(x=810, y=2, width=640, height=600)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=10, width=627, height=400)

        img_right = Image.open(r"images\rightf.jpg")
        img_right = img_right.resize((620, 150), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=420, width=620, height=120)

        # ---------------------------------------------------------scroll bar and table----------------------------------------------------------
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ------------------------------------------------------------------fetch data---------------------------------------------------------------

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    # ------------------------------------------------------------------import csv----------------------------------------------------------------

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            print(mydata)
            self.fetchData(mydata)
    # --------------------------------------------------------------------export csv--------------------------------------------------------------

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Date", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv*"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Your data exported to "+os.path.basename(fln)+"succesfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)
    # ----------------------------------------------------------------------get coursor-----------------------------------------------------------

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


# -------------------------------------------------------------------------reset data-------------------------------------------------------------

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
