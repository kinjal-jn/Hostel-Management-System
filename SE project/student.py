from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class stu_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1363x550+0+160")
        
        #**********************Variables*************************
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_Name=StringVar()
        self.var_Mothers_name=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact_no=StringVar()
        self.var_Gmail=StringVar()
        self.var_Semester=StringVar()
        self.var_ID_proof=StringVar()
        self.var_Id_no=StringVar()
        self.var_Address=StringVar()
         


        #**********************title*************************
        lbl_title=Label(self.root,text="ENTER STUDENT DETAILS",font=("arial",18,"bold"),bg="cyan2",fg="blue4",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1363,height=50)


        #**********************logo *************************
        img2=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img2=img2.resize((90,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=45)


        #**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("arial",20,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #**********************labels and entries*************************
        # student roll no.
        lbl_stu_ref=Label(labelframeleft,text="Ref no.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_stu_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)
        
        # student name
        sname=Label(labelframeleft,text="Student Name",font=("arial",12,"bold"),padx=2,pady=6)
        sname.grid(row=1,column=0,sticky=W)

        txtsname=ttk.Entry(labelframeleft,textvariable=self.var_Name,width=29,font=("arial",13,"bold"))
        txtsname.grid(row=1,column=1)
        
        # Mothers name
        lblmname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_Mothers_name,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
        # GENDER
        label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_Gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("CHOOSE","MALE","FEMALE","RATHER NOT SAY")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # CONTACT no.
        lblphone=Label(labelframeleft,text="Contact No.",font=("arial",12,"bold"),padx=2,pady=6)
        lblphone.grid(row=4,column=0,sticky=W)
        txtphone=ttk.Entry(labelframeleft,textvariable=self.var_Contact_no,width=29,font=("arial",13,"bold"))
        txtphone.grid(row=4,column=1)

        # Gmail
        lblEmail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=5,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_Gmail,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=5,column=1)

        # Semester
        lblSem=Label(labelframeleft,text="Semester:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSem.grid(row=6,column=0,sticky=W)
        combo_sem=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_Semester,width=27,state="readonly")
        combo_sem["value"]=("CHOOSE","I","II","III","IV","V","VI")
        combo_sem.current(0)
        combo_sem.grid(row=6,column=1)

        # ID proof
        lblID=Label(labelframeleft,text="ID proof type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblID.grid(row=7,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_ID_proof,width=27,state="readonly")
        combo_id["value"]=("CHOOSE","Adhar Card","Driving License","PAN Card","Other")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)

        #ID number
        lblIDno=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIDno.grid(row=8,column=0,sticky=W)
        txtIDno=ttk.Entry(labelframeleft,textvariable=self.var_Id_no,width=29,font=("arial",13,"bold"))
        txtIDno.grid(row=8,column=1)

        #Resident Address
        lblAdd=Label(labelframeleft,text="Resident Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblAdd.grid(row=9,column=0,sticky=W)
        txtAdd=ttk.Entry(labelframeleft,textvariable=self.var_Address,width=29,font=("arial",13,"bold"))
        txtAdd.grid(row=9,column=1)


        #**********************btns*************************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        #**********************Table Frame search system*************************
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & search system",font=("arial",20,"bold"))
        Table_Frame.place(x=435,y=50,width=900,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","ref")
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
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Stu_Details_Table=ttk.Treeview(details_table,column=('Ref','Name','Mothers name','Gender','Contact no','Gmail','Semester','ID proof','Id no','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Stu_Details_Table.xview)
        scroll_y.config(command=self.Stu_Details_Table.yview)

        self.Stu_Details_Table.heading("Ref",text="Ref")
        self.Stu_Details_Table.heading("Name",text="Name")
        self.Stu_Details_Table.heading("Mothers name",text="Mother Name")
        self.Stu_Details_Table.heading("Gender",text="Gender")
        self.Stu_Details_Table.heading("Contact no",text="Contact No")
        self.Stu_Details_Table.heading("Gmail",text="Gmail")
        self.Stu_Details_Table.heading("Semester",text="Semester")
        self.Stu_Details_Table.heading("ID proof",text="ID proof")
        self.Stu_Details_Table.heading("Id no",text="ID Number")
        self.Stu_Details_Table.heading("Address",text="Address.")

        self.Stu_Details_Table['show']='headings'

        self.Stu_Details_Table.column("Ref",width=100)
        self.Stu_Details_Table.column("Name",width=100)
        self.Stu_Details_Table.column("Mothers name",width=100)
        self.Stu_Details_Table.column("Gender",width=100)
        self.Stu_Details_Table.column("Contact no",width=100)
        self.Stu_Details_Table.column("Gmail",width=100)
        self.Stu_Details_Table.column("Semester",width=100)
        self.Stu_Details_Table.column("ID proof",width=100)
        self.Stu_Details_Table.column("Id no",width=100)
        self.Stu_Details_Table.column("Address",width=100)


        self.Stu_Details_Table.pack(fill=BOTH,expand=1)
        self.Stu_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # Adding data to the Mysql database
    def add_data(self):
        if self.var_Contact_no.get()=="" or self.var_Mothers_name.get()=="":
            messagebox.showerror("Error","Please fill all the fields.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_Name.get(),
                                                                                        self.var_Mothers_name.get(),
                                                                                        self.var_Gender.get(),
                                                                                        self.var_Contact_no.get(),
                                                                                        self.var_Gmail.get(),
                                                                                        self.var_Semester.get(),
                                                                                        self.var_ID_proof.get(),
                                                                                        self.var_Id_no.get(),
                                                                                        self.var_Address.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    # Fetching fata into the table from database  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_children())
            for i in rows:
                self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()  


    # Getting data into details when entry field is selected
    def get_cursor(self,event=""):
        cursor_row=self.Stu_Details_Table.focus()
        content=self.Stu_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_Name.set(row[1])
        self.var_Mothers_name.set(row[2])
        self.var_Gender.set(row[3])
        self.var_Contact_no.set(row[4])
        self.var_Gmail.set(row[5])
        self.var_Semester.set(row[6])
        self.var_ID_proof.set(row[7])
        self.var_Id_no.set(row[8])
        self.var_Address.set(row[9])


    # Update button
    def update(self):
        if self.var_Contact_no.get()=="":
            messagebox.showerror("Error","Please enter Contact no.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set Name=%s, Mother=%s, Gender=%s, Contact=%s, Gmail=%s, Semester=%s, IDproof=%s, IDno=%s, Address=%s where Ref=%s",(
                                                                                        self.var_Name.get(),
                                                                                        self.var_Mothers_name.get(),
                                                                                        self.var_Gender.get(),
                                                                                        self.var_Contact_no.get(),
                                                                                        self.var_Gmail.get(),
                                                                                        self.var_Semester.get(),
                                                                                        self.var_ID_proof.get(),
                                                                                        self.var_Id_no.get(),
                                                                                        self.var_Address.get(),
                                                                                        self.var_ref.get()
                                                                                        ))
                                                                                                                                                                        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Student details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this student?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query="delete from student where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_Name.set(""),
        self.var_Mothers_name.set(""),
        # self.var_Gender.set(""),
        self.var_Contact_no.set(""),
        self.var_Gmail.set(""),
        # self.var_Semester.set(""),
        # self.var_ID_proof.set(""),
        self.var_Id_no.set(""),
        self.var_Address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0: 
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_children())
            for i in rows:
                self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
  
    


if __name__ == "__main__":
    root=Tk()
    obj=stu_Win(root)
    root.mainloop()  