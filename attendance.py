from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class attendance:
 def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognitiion")
#variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

#image 1
        img=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img2.jpg")
        img=img.resize((500,150))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #image 2
        img1=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img1.jpg")
        img1=img1.resize((500,150))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

         #background image
        img3=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img5.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

         #title
        title_lbl=Label(bg_img,text="ATTENDANCE",font=("candara",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img, bd = 2 )
        main_frame.place(x=10,y=50,width=1500,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame, bd = 2 ,bg="white",relief=RIDGE, text="Student Attendance Details",font=("candara",12))
        Left_frame.place( x = 10 , y = 10 ,width=760,height=580)

        img_left=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img5.jpg")
        img_left=img_left.resize((650,290))
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place( x = 5 , y = 0, width=720,height = 130)


        left_inside_frame=Frame(Left_frame, bd = 2 )
        left_inside_frame.place(x=0,y=200,width=750,height=400)

        #Labeland entry
        #attendance id

        attendanceid_label=Label(left_inside_frame, text="Attendance ID:", font=("candara",12), bg="white") 
        attendanceid_label.grid(row=0,column=0,padx=10, sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("candara",12))
        attendanceid_entry.grid(row=0,column=1,padx=10,sticky=W)

        #roll

        rollLabel=Label(left_inside_frame,text="Roll:",bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold") 
        atten_roll.grid(row=0,column=3, pady=8)

        # name

        nameLabel=Label(left_inside_frame, text="Name:",bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold") 
        atten_name.grid(row=1,column=1, pady=0)

        # Department

        depLabel=Label(left_inside_frame, text="Department:",bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)
        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_department,font="comicsansns 11 bold") 
        atten_dep.grid(row=1,column=3,pady=8)

        #time

        timeLabel=Label(left_inside_frame, text="Time:",bg="white", font="comicsansns 11 bold") 
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1,pady=8)

        #Date

        dateLabel=Label (left_inside_frame, text="Date:",bg="white", font="comicsansns 11 bold") 
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold") 
        atten_date.grid(row=2,column=3,pady=8)

        # attendance

        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold") 
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold", state="readonly") 
        self.atten_status["values"]=("Status","Present","Absent")

        self.atten_status.grid(row=3, column=1,pady=8) 
        self.atten_status.current(0)

        #button frames

        btn_frame=Frame(left_inside_frame,bd=2, relief=RIDGE, bg="white") 
        btn_frame.place(x=0,y=300,width=715,height=70)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17, font=("candara",12), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text="export csv",command=self.exportCsv,width=17, font=("candara",12), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame, text="Update", width=17, font=("candara",12), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("candara",12), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)


         #  right frame
        Right_frame=LabelFrame(main_frame, bd = 2 ,bg="white",relief=RIDGE, text="Attendance  Details",font=("candara",12))
        Right_frame.place( x = 750 , y = 10 ,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2, relief=RIDGE, bg="white") 
        table_frame.place(x=5,y=5,width=700,height=455)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#fetch data
 def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
                self.AttendaceReportTable.insert("", END, values=i)
#import csv
 def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV  file","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                        mydata.append(i)
                self.fetchData(mydata)


#export csv
 def exportCsv(self):
        try:
                if len(mydata)<1:
                      messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                      return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV  file","*.csv"),("ALL File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="")as myfile:
                      exp_write=csv.writer(myfile,delimiter=",")
                      for i in mydata:
                             exp_write.writerow(i)
                             messagebox.showinfo("Data export","Your data exported to"+os.path.basename(fln)+"Sucessfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
 def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable(cursor_row)
        rows=content['values']
        self.var_atten_id(rows[0])
        self.var_atten_roll(rows[1])
        self.var_atten_name(rows[2])
        self.var_atten_department(rows[3])
        self.var_atten_time(rows[4])
        self.var_atten_date(rows[5])
        self.var_atten_attendance(rows[6])


 def reset_data(self):
        self.var_atten_id("")
        self.var_atten_roll("")
        self.var_atten_name("")
        self.var_atten_department("")
        self.var_atten_time("")
        self.var_atten_date("")
        self.var_atten_attendance("")
                       

        

if __name__ == "__main__":
        root=Tk()
        obj=attendance(root)
        root.mainloop()