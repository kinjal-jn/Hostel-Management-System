from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class room_maintenance:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1363x550+0+160") 

        #********************Variables**********************
        self.var_contact=StringVar()
        self.var_roomNo=StringVar()
        self.var_problem=StringVar()
        self.var_feedback=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        


        #**********************title*************************
        lbl_title=Label(self.root,text="ROOM MAINTENANCE",font=("arial",18,"bold"),bg="cyan2",fg="blue4",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1363,height=50)


        #**********************logo *************************
        img=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img=img.resize((90,45),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=45)

        #**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Maintenance",font=("arial",20,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=470)

        #**********************labels and entries*************************
        # student contact no.
        lbl_stu_contact=Label(labelframeleft,text="Student Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_stu_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # fetch data button
        btnFetchdata=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnFetchdata.place(x=325,y=2)


        # Room no. 
        lbl_Roomno=Label(labelframeleft,text="Room No.:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Roomno.grid(row=1,column=0,sticky=W)

        txtRoomno=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=29,font=("arial",13,"bold"))
        txtRoomno.grid(row=1,column=1)

        # Problem
        lbl_Problem=Label(labelframeleft,text="Problem:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Problem.grid(row=2,column=0,sticky=W)

        combo_Problem=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_problem,width=27,state="readonly")
        combo_Problem["value"]=("Select","House Keeping","Electrical","Carpentry","Plumbing","Mess Feedback","other")
        combo_Problem.current(0)
        combo_Problem.grid(row=2,column=1)

        # time
        time=Label(labelframeleft,text="Suitable Time",font=("arial",12,"bold"),padx=2,pady=6)
        time.grid(row=3,column=0,sticky=W)
        #txttime=ttk.Entry(labelframeleft,textvariable=self.var_time,width=29,font=("arial",13,"bold"))
        #txttime.grid(row=3,column=1)

        combo_RoomNo=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_time,width=27,state="readonly")
        combo_RoomNo["value"]=("Select","Morning","Afternoon","Evening")
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=3,column=1)

       # Date
        lbl_date=Label(labelframeleft,text="Preferred date :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_date.grid(row=4,column=0,sticky=W)
        txtdate=ttk.Entry(labelframeleft,textvariable=self.var_date,width=29,font=("arial",13,"bold"))
        txtdate.grid(row=4,column=1)

        # feedback
        lbl_feedback=Label(labelframeleft,text="Feedback:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_feedback.grid(row=5,column=0,sticky=W)
        txtfeedback=ttk.Entry(labelframeleft,textvariable=self.var_feedback,width=29,font=("arial",13,"bold"))
        txtfeedback.grid(row=5,column=1)


        #**********************btns*************************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=320,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #**********************Right side image*************************
        img3=Image.open(r"C:\Users\admin\Desktop\SE project\photos\housekeeping.jpg")
        img3=img3.resize((500,210),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=830,y=53,width=500,height=210)

        #**********************Table Frame search system*************************
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & search system",font=("arial",20,"bold"))
        Table_Frame.place(x=435,y=260,width=900,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)


        #**********************show data in Table*************************
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=47,width=860,height=170)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_Table=ttk.Treeview(details_table,column=('contact','roomNo','problem','time','date'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("contact",text="Contact")
        self.Room_Table.heading("roomNo",text="roomNo")
        self.Room_Table.heading("problem",text="problem")
        self.Room_Table.heading("time",text="time")
        self.Room_Table.heading("date",text="date")

        self.Room_Table['show']='headings'

        self.Room_Table.column("contact",width=100)
        self.Room_Table.column("roomNo",width=100)
        self.Room_Table.column("problem",width=100)
        self.Room_Table.column("time",width=100)
        self.Room_Table.column("date",width=100)
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


    # add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_roomNo.get()=="":
            messagebox.showerror("Error","Please fill all the fields.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room_maintain values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_roomNo.get(),
                                                                                        self.var_problem.get(),
                                                                                        self.var_time.get(),
                                                                                        self.var_date.get()
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success","Complaint loged",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    # Fetching fata into the table from database  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room_maintain")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get cursor

    def get_cursor(self,event=""):
        cursor_row=self.Room_Table.focus()
        content=self.Room_Table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_problem.set(row[2]),
        self.var_time.set(row[3]),
        self.var_date.set(row[4])

    # Update button
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact no.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room_maintain set roomNo=%s, problem=%s, time=%s, date=%s where contact=%s",(
                                                                                        
                                                                                        self.var_roomNo.get(),
                                                                                        self.var_problem.get(),
                                                                                        self.var_time.get(),
                                                                                        self.var_date.get(),
                                                                                        self.var_contact.get()
                                                                                        ))
                                                                                                                                                                        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room maintenance details has been updated successfully",parent=self.root)
    
    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this complaint?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query="delete from room_maintain where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset function
    def reset(self):
        self.var_contact.set("")
        self.var_roomNo.set("")
        self.var_problem.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_feedback.set("")
       


    #****************************** All data fetch***********************

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact no.")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query=("select Name from student where Contact=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","This number is NOT found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=350,height=200)

                #**************************name*********************
                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=0)

                #**************************Mothers name*********************
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                query=("select Mother from student where Contact=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Mother's name:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=30)

                #**************************Gender*********************
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from student where Contact=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=60)

                #**************************gmail*********************
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                query=("select Gmail from student where Contact=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gmail:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=90)

                #**************************semester*********************
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                query=("select Semester from student where Contact=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Semester:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=120)

                #**************************address*********************
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                query=("select Address from student where Contact=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=150)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=120,y=150)

    # search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room_maintain where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0: 
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


        



if __name__ == "__main__":
    root=Tk()
    obj=room_maintenance(root)
    root.mainloop()