from tkinter import*
from PIL import Image,ImageTk
from student import stu_Win
from room import Roombooking
from details import DetailsRoom
from maintainence import room_maintenance

class HostelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1550x800+0+0")

        #********************first image*******************
        img1=Image.open(r"C:\Users\admin\Desktop\SE project\photos\name.jpg")
        img1=img1.resize((1135,140),Image.Resampling.LANCZOS )
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=230,y=0,width=1135,height=140)


        #**********************logo*************************
        img2=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        #**********************label**************************
        lbl_title=Label(self.root,text="HOSTEL MANAGEMENT SYSTEM",font=("times new roman",28,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1368,height=50)


        #**********************main frame************************
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        main_frame.place(x=0,y=190,width=1550,height=620)


        #**********************menu ************************
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=228)

        #**********************btn frame************************
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        std_btn=Button(btn_frame,text="STUDENT DETAILS",command=self.stu_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        std_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM BOOKING",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)


        details_btn=Button(btn_frame,text="ADMIN",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        

        report_btn=Button(btn_frame,text="MAINTENANCE",command=self.room_maintain,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #**********************right side img************************
        img3=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc campus.jpeg")
        img3=img3.resize((1130,497),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=225,y=0,width=1135,height=510)

        


    def stu_details(self):
        self.new_window=Toplevel(self.root)
        self.app=stu_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
    
    def room_maintain(self):
        self.new_window=Toplevel(self.root)
        self.app=room_maintenance(self.new_window)

          

if __name__ == "__main__":
    root=Tk()
    obj=HostelManagementSystem(root)
    root.mainloop()