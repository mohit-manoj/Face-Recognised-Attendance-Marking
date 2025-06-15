'''from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognitiion")

        title_lbl=Label(self.root,text="DEVELOPER",font=("candara",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img3.jpg")
        img_top=img_top.resize((1530,720))
        self.photoimg_top=ImageTk. PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place( x = 0 , y = 55, width=1530,height = 720)
        #FRAME

        main_frame=Frame(f_lbl, bd = 2 )
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"C:\Users\91944\OneDrive\Desktop\Face Recognition\collage\img3.jpg")
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk. PhotoImage(img_top)
        f_lbl=Label(main_frame,image=self.photoimg_top)
        f_lbl.place( x =300, y=0, width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="content adikkan olla space video :9 - 11:59", font=("candara",12), bg="white")
        dev_label.place(x=0,y=5)



if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()'''