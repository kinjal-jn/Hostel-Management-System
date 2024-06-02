from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import warnings
from tkinter import messagebox
import mysql.connector
import random
from student import stu_Win
from room import Roombooking
from details import DetailsRoom
from maintainence import room_maintenance


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry('1550x800+0+0')

        #********************first image*******************
        img1=Image.open(r"C:\Users\admin\Desktop\SE project\photos\loginpage.jpg")
        img1=img1.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)

        frame=Frame(self.root,bg="white",border=5,relief="solid")
        frame.place(x=810,y=120,width=340,height=450)

        img1=Image.open(r"C:\Users\admin\Desktop\SE project\photos\new user.jpg")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=930,y=125,width=100,height=100)

        get_str=Label(frame,text="GET STARTED",font=("Courier",20,"bold"),fg="DodgerBlue4",bg="white")
        get_str.place(x=75,y=95)

        #label
        username_lbl=Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtuser.place(x=40,y=180,width=270,height=30)

        password_lbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtpass.place(x=40,y=250,width=270,height=30)

        # icon images

        img2=Image.open(r"C:\Users\admin\Desktop\SE project\photos\loginlogo.jpg")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=860,y=278,width=25,height=25)

        img3=Image.open(r"C:\Users\admin\Desktop\SE project\photos\loginlogo.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3img3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3img3,bg="black",borderwidth=0)
        lblimg3.place(x=860,y=348,width=25,height=25)

        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="DodgerBlue4",activeforeground="white",activebackground="DodgerBlue4")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # registration btn
        registerbtn=Button(frame,text="New User",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="DodgerBlue4",bg="white",activeforeground="DodgerBlue4",activebackground="white")
        registerbtn.place(x=5,y=350,width=160)

        #forgot password
        forgot_pass_btn=Button(frame,command=self.forgot_password_window,text="Forgot Password",font=("times new roman",13,"bold"),borderwidth=0,fg="DodgerBlue4",bg="white",activeforeground="DodgerBlue4",activebackground="white")
        forgot_pass_btn.place(x=32,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HostelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    #reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query1=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset")



    # forgot pass window

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter valid Email")
            else:
                conn.close()    
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+810+120")
                

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="DodgerBlue4",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth place","Your Fav food","Your Gender","Your Fav book")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="DodgerBlue4",fg="white")
                btn.place(x=100,y=290)








##################################################################################################

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # background image
        img1=Image.open(r"C:\Users\admin\Desktop\SE project\photos\register-background.jpg")
        img1=img1.resize((1500,700),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1500,height=700)

        # left img

        img2=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img2=img2.resize((470,550),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RAISED)
        lblimg2.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="DodgerBlue4",bg="white")
        register_lbl.place(x=20,y=20)

        # labels and entry

        # row one
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        Lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        Lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # row two

        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        fname=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # row 3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth place","Your Fav food","Your Gender","Your Fav book")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # row 4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        fname=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=370,y=310)

        self.txt_confpass=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confpass.place(x=370,y=340,width=250)

        ## check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to all the terms & conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # buttons
        img=Image.open(r"C:\Users\admin\Desktop\SE project\photos\registerButton.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=50,y=420,width=200)

        img3=Image.open(r"C:\Users\admin\Desktop\SE project\photos\login button.jpg")
        img3=img3.resize((100,60),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b2=Button(frame,image=self.photoimg3,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b2.place(x=300,y=415,width=100)


    # function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirmation unmatched")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succcess","Registered successfully")


########################################################################################
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
    main()