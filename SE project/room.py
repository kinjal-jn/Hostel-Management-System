from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1363x550+0+160") 

        #********************Variables**********************
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        #**********************title*************************
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("arial",18,"bold"),bg="cyan2",fg="blue4",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1363,height=50)


        #**********************logo *************************
        img=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img=img.resize((90,45),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=45)

        #**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",20,"bold"),padx=2)
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


        # check_in date 
        lbl_Check_in=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_in.grid(row=1,column=0,sticky=W)

        txtCheck_in=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtCheck_in.grid(row=1,column=1)

        # Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=27,state="readonly")
        combo_RoomType["value"]=ide
        # combo_RoomType.current(0)
        combo_RoomType.grid(row=2,column=1)

        # Available room 
        RoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        RoomAvailable.grid(row=3,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=3,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomavailable,width=27,state="readonly")
        combo_RoomNo["value"]=rows
        # combo_RoomNo.current(0)
        combo_RoomNo.grid(row=3,column=1)

        # meal
        lbl_Meal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=4,column=0,sticky=W)
        combo_meal=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_meal,width=27,state="readonly")
        combo_meal["value"]=("CHOOSE","VEG","NON-VEG")
        combo_meal.current(0)
        combo_meal.grid(row=4,column=1)

        # Paid tax
        lbl_PaidTax=Label(labelframeleft,text="Paid Tax(2.5%):",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_PaidTax.grid(row=5,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtPaidTax.grid(row=5,column=1)

        # Sub total
        lbl_SubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_SubTotal.grid(row=6,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtSubTotal.grid(row=6,column=1)

        # Total Cost
        lbl_TotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_TotalCost.grid(row=7,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtTotalCost.grid(row=7,column=1)

        #********************** bill btn*************************
        btnbill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnbill.grid(row=8,column=0,padx=1,sticky=W)

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
        img3=Image.open(r"C:\Users\admin\Desktop\SE project\photos\room.jpg")
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

        self.Room_Table=ttk.Treeview(details_table,column=('Contact','CheckIn','RoomType','RoomAvailable','Meal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("Contact",text="Contact")
        self.Room_Table.heading("CheckIn",text="CheckIn")
        self.Room_Table.heading("RoomType",text="RoomType")
        self.Room_Table.heading("RoomAvailable",text="RoomAvailable")
        self.Room_Table.heading("Meal",text="Meal")

        self.Room_Table['show']='headings'

        self.Room_Table.column("Contact",width=100)
        self.Room_Table.column("CheckIn",width=100)
        self.Room_Table.column("RoomType",width=100)
        self.Room_Table.column("RoomAvailable",width=100)
        self.Room_Table.column("Meal",width=100)
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


    # add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Please fill all the fields.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get()
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    # Fetching fata into the table from database  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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
        self.var_checkin.set(row[1]),
        self.var_roomtype.set(row[2]),
        self.var_roomavailable.set(row[3]),
        self.var_meal.set(row[4])

    # Update button
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact no.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s, roomtype=%s, roomavailable=%s, meal=%s where contact=%s",(
                                                                                        
                                                                                        self.var_checkin.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_contact.get()
                                                                                        ))
                                                                                                                                                                        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
    
    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this room detail?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
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
        self.var_checkin.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


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
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0: 
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        #inDate=self.var_checkin.get()
        #indate=datetime.strptime(indate,"%d/%m/%Y")

        if (self.var_meal.get()=="VEG" and self.var_roomtype.get()=="SINGLE"):
            q1=float(650)
            q2=float(4500)
            q3=float(q1+q2)
            Tax="Rs."+str("%.2f"%((q3)*0.025))
            ST="Rs."+str("%.2f"%((q3)))
            TT="Rs."+str("%.2f"%(q3+((q3)*0.025)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="VEG" and self.var_roomtype.get()=="COMBINED"):
            q1=float(650)
            q2=float(3000)
            q3=float(q1+q2)
            Tax="Rs."+str("%.2f"%((q3)*0.025))
            ST="Rs."+str("%.2f"%((q3)))
            TT="Rs."+str("%.2f"%(q3+((q3)*0.025)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="NON-VEG" and self.var_roomtype.get()=="COMBINED"):
            q1=float(920)
            q2=float(3000)
            q3=float(q1+q2)
            Tax="Rs."+str("%.2f"%((q3)*0.025))
            ST="Rs."+str("%.2f"%((q3)))
            TT="Rs."+str("%.2f"%(q3+((q3)*0.025)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="NON-VEG" and self.var_roomtype.get()=="SINGLE"):
            q1=float(920)
            q2=float(4500)
            q3=float(q1+q2)
            Tax="Rs."+str("%.2f"%((q3)*0.025))
            ST="Rs."+str("%.2f"%((q3)))
            TT="Rs."+str("%.2f"%(q3+((q3)*0.025)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="NON-VEG" and self.var_roomtype.get()=="SINGLE"):
            q1=float(920)
            q2=float(4500)
            q3=float(q1+q2)
            Tax="Rs."+str("%.2f"%((q3)*0.025))
            ST="Rs."+str("%.2f"%((q3)))
            TT="Rs."+str("%.2f"%(q3+((q3)*0.025)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        



if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop() 