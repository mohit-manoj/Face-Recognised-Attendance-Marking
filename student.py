from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognitiion")

        #variable

        self.var_department=StringVar()

        self.var_course=StringVar()

        self.var_year=StringVar()

        self.var_semester=StringVar()

        self.va_id=StringVar()

        self.var_name=StringVar()

        self.var_division=StringVar()

        self.var_RollNo=StringVar()

        self.var_Gender=StringVar()

        self.var_DOB=StringVar()


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

        #image 3
        img2=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img4.jpg")
        img2=img2.resize((500,150))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=150)

        #background image
        img3=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img5.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("candara",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img, bd = 2 )
        main_frame.place(x=10,y=50,width=1500,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame, bd = 2 ,bg="white",relief=RIDGE, text="Student Details",font=("candara",12))
        Left_frame.place( x = 10 , y = 10 ,width=760,height=580)

        img_left=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img5.jpg")
        img_left=img_left.resize((650,290))
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place( x = 5 , y = 0, width=720,height = 130)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current course information",font=("candara",12))
        current_course_frame.place(x=5,y=135,width=720,height=125)

        # Department
        dep_label=Label(current_course_frame,text="Department", font=("candara",12), bg="white")
        dep_label.grid(row=0,column=0,padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department, font=("candara",12), state="readonly",width=20)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Civil", "Mechnical","Artificial Intelligence","Unknown")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W)

        # Course
        course_label=Label(current_course_frame, text="Course", font=("candara",12),bg="white")
        course_label.grid(row=0,column=2,padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman",13,"bold"), state="readonly",width=20)
        course_combo ["values"]=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)    

        # Year
        year_label=Label(current_course_frame, text="Year", font=("candara",12),bg="white") 
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"]=("Select Year", "2020-21","2021-22","2022-23", "2023-24") 
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10, sticky=W)

        # Semester
        semester_label=Label(current_course_frame, text="Semester", font=("candara",12), bg="white") 
        semester_label.grid(row=1,column=2,padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("candara",12), state="readonly",width=20)
        semester_combo ["values"]=("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2, pady=10, sticky=W)   

        # class student info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Class student information",font=("candara",12))
        class_Student_frame.place(x=5,y=250,width=720,height=300)

        #student id
        studentid_label=Label(class_Student_frame, text="Student ID:", font=("candara",12), bg="white") 
        studentid_label.grid(row=0,column=0,padx=10, sticky=W)

        studentid_entry=ttk.Entry(class_Student_frame,textvariable=self.va_id,width=20,font=("candara",12))
        studentid_entry.grid(row=0,column=1,padx=10, sticky=W)

        # student name

        studenName_label=Label(class_Student_frame, text="Student Name:", font=("candara",12), bg="white")
        studenName_label.grid(row=0,column=2,padx=10, pady=5, sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name, width=20, font=("candara",12))
        studentName_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)

        # class division
        
        class_div_label=Label(class_Student_frame, text="Class Division:", font=("candara",12), bg="white") 
        class_div_label.grid(row=1,column=0,padx=10, pady=5, sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_division, font=("times new roman", 13, "bold"), state="readonly", width=18)
        div_combo["values"]=("A", "B","C") 
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5, sticky=W)


        # Roll No

        roll_no_label=Label(class_Student_frame, text="RollNo: ", font=("candara",12), bg="white")
        roll_no_label.grid(row=1, column=2,padx=10,pady=5, sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_RollNo,width=20,  font=("candara",12)) 
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5, sticky=W)

        # Gender

        gender_label=Label(class_Student_frame, text="Gender:",  font=("candara",12), bg="white") 
        gender_label.grid(row=2,column=0,padx=10, pady=5, sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_Gender, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"]=("Male", "Female") 
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5, sticky=W)


        # Date of birth

        dob_label=Label(class_Student_frame, text="DOB:",  font=("candara",12),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5, sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_DOB,width=20,  font=("candara",12)) 
        dob_entry.grid(row=2,column=3,padx=10, pady=5, sticky=W)

        # Email

        #email_label=Label(class_Student_frame, text="Email:",  font=("candara",12), bg="white")
        #email_label.grid(row=3,column=0,padx=10, pady=5, sticky=W)

        #email_entry=ttk.Entry(class_Student_frame, width=20,  font=("candara",12))
        #email_entry.grid(row=3,column=1,padx=10,pady=5, sticky=W)

        # radio Buttons

        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6,column=1)

        # buttons frame

        btn_frame=Frame(class_Student_frame,bd=2, relief=RIDGE, bg="white") 
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=17, font=("candara",12), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text="Update", command=self.update_data, width=17, font=("candara",12), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("candara",12), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset", width=17,command=self.reset_data, font=("candara",12), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame, bd=2, relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample", width=35, font=("candara",12), bg="blue", fg="white") 
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample", width=35, font=("candara",12), bg="blue", fg="white") 
        update_photo_btn.grid(row=0,column=1)


        #  right frame
        Right_frame=LabelFrame(main_frame, bd = 2 ,bg="white",relief=RIDGE, text="Student Details",font=("candara",12))
        Right_frame.place( x = 750 , y = 10 ,width=720,height=580)

        img_right=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img3.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk. PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place( x = 5 , y = 0, width=720,height = 130)

        #search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white", relief=RIDGE, text="Search System",font=("candara",12))
        search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(search_frame, text="Search Bar:",  font=("candara",15), bg="light blue")
        search_label.grid(row=0,column=0,padx=10, pady=5, sticky=W)

        search_combo=ttk.Combobox(search_frame, font=("candara",12), state="readonly",width=20)
        search_combo["values"]=("Select", "RollNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame,width=11,  font=("candara",12)) 
        search_entry.grid(row=0,column=2,padx=10, pady=5, sticky=W)

        search_btn=Button(search_frame, text="Search", width=12, font=("candara",12), bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame, text="Show All", width=12, font=("candara",12), bg="blue", fg="white")
        showall_btn.grid(row=0,column=4,padx=4) 

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("department","course","year","semester","id","name","division","RollNo","Gender","DOB","photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #function declaration
 
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.va_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                    self.var_department.get(),  
                                                                                    self.var_course.get(),

                                                                                    self.var_year.get(),

                                                                                    self.var_semester.get(),

                                                                                    self.va_id.get(),

                                                                                    self.var_name.get(),

                                                                                    self.var_division.get(),

                                                                                    self.var_RollNo.get(),

                                                                                    self.var_Gender.get(),

                                                                                    self.var_DOB.get(), 
                                                                                    self.var_radio1.get()
                                                                                ))
                                                                
                                                                             
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added succesfully",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:

            self.student_table.delete(*self.student_table.get_children())

            for i in data:

                self.student_table.insert("",END, values=i)

            conn.commit()

        conn.close()

    #get cursor

    def get_cursor(self,event=""):

        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]), 
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]),
        self.va_id.set(data[4]),  
        self.var_name.set(data[5]),
        self.var_division.set(data[6]),
        self.var_RollNo.set(data[7]), 
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]), 
        self.var_radio1.set(data[10])
         
    #update fun

    def update_data(self):
        if (
        self.var_department.get()=="Select Department" 
        or self.var_name.get()=="" 
        or self.va_id.get()==""
    ):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                    Update=messagebox.askyesno("Update","do you want to Update this details",parent=self.root)
                    if Update>0:
                        conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc", database="face_recognition")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,RollNo=%s,Gender=%s,DOB=%s,PhotoSample=%s where id=%s",(

                                                                                                        self.var_department.get(),  
                                                                                                        self.var_course.get(),

                                                                                                        self.var_year.get(),

                                                                                                        self.var_semester.get(),

                                                                                                        self.var_name.get(),

                                                                                                        self.var_division.get(),

                                                                                                        self.var_RollNo.get(),

                                                                                                        self.var_Gender.get(),

                                                                                                        self.var_DOB.get(), 
                                                                                                        self.var_radio1.get(),
                                                                                                        self.va_id.get() 
                                    
                                                                                                    ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("success","student detalis update completed",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)
#delete function
    def delete_data(self):
        if self.va_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc", database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.va_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#reset
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_semester.set("Select semester")
        self.va_id.set("")
        self.var_name.set("")
        self.var_division.set("Select Division")
        self.var_RollNo.set("")
        self.var_Gender.set("Male")
        self.var_DOB.set("")
        self.var_radio1.set("")

        #generate data set or take photo sample

    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.va_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Dku3xwmfmc", database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,RollNo=%s,Gender=%s,DOB=%s,PhotoSample=%s where id=%s",(

                                                                                                        self.var_department.get(),  
                                                                                                        self.var_course.get(),

                                                                                                        self.var_year.get(),

                                                                                                        self.var_semester.get(),

                                                                                                        self.var_name.get(),

                                                                                                        self.var_division.get(),

                                                                                                        self.var_RollNo.get(),

                                                                                                        self.var_Gender.get(),

                                                                                                        self.var_DOB.get(), 
                                                                                                        self.var_radio1.get(),
                                                                                                        self.va_id.get() ==id+1
                                    
                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    #load predefined

                    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_cascade.detectMultiScale(gray,1.3,5)

                        #scaling factor=1.3

                        #Minimum Neighbor=5

                        for (x,y,w,h) in faces:

                            face_cropped=img[y:y+h,x:x+w]

                            return face_cropped

                    cap = cv2.VideoCapture(0)  # Try different backends


                    img_id = 0  # Reset img_id to 0 at the beginning
                    while True:
                        ret, my_frame = cap.read()

                        # Face detection logic
                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1

                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            file_name_path = f"data/user.{id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)

                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        # Check for exit conditions
                        if cv2.waitKey(1) == 13 or img_id == 333:  # Change img_id == 10 for testing
                            break

                    # Release video capture and destroy windows outside the loop
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!")

            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()
