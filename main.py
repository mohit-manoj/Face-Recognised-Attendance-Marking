from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition1
from help import Help
from attendance import attendance


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognitiion")

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
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("candara",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\student.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,command=self.Student_details, cursor="hand2")
        b1.place( x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.Student_details, cursor="hand2",font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=200,y=300,width=220,height=40)

        #face detect button
        img5=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img13.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place( x=500,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Face Detector", cursor="hand2",command=self.face_data,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=500,y=300,width=220,height=40)

        #attendance button
        img6=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img8.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place( x=800,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=800,y=300,width=220,height=40)

        #Help desk button
        img7=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img10.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place( x=1100,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=1100,y=300,width=220,height=40)

        #Train Data button
        img8=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img11.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place( x=200,y=380,width=220,height=220)
        b1_1=Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=200,y=580,width=220,height=40)

        #Photos button
        img9=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img7.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place( x=500,y=380,width=220,height=220)
        b1_1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=500,y=580,width=220,height=40)

        #Developer button
        imgq=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img9.jpg")
        imgq=imgq.resize((220,220))
        self.photoimgq=ImageTk.PhotoImage(imgq)
        
        b1=Button(bg_img, image=self.photoimgq, cursor="hand2")
        b1.place( x=800,y=380,width=220,height=220)
        b1_1=Button(bg_img,text="Developer", cursor="hand2",font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=800,y=580,width=220,height=40)

        #Exit button
        imgw=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img12.jpg")
        imgw=imgw.resize((220,220))
        self.photoimgw=ImageTk.PhotoImage(imgw)
        
        b1=Button(bg_img, image=self.photoimgw, cursor="hand2",command=self.iexit)
        b1.place( x=1100,y=380,width=220,height=220)
        b1_1=Button(bg_img,text="Exit", cursor="hand2",command=self.iexit,font=("candara",15),bg="darkblue",fg="white")
        b1_1.place( x=1100,y=580,width=220,height=40)

    def open_img(self):
         os.startfile("data")


    def iexit(self):
        self.iexit=tkinter.Message.askyesorno("Face recognition","Are you sure you want to exit",parent=self.root)
        if self.iexit>0:
           self.root.destroy()
        else:
            return


        #func

    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition1(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)





 
if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()
