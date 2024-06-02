from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1363x550+0+160") 

        #**********************title*************************
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("arial",18,"bold"),bg="cyan2",fg="blue4",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1363,height=50)
        lbl_title=Label(self.root,text="ONLY TO BE ACCESSED BY ADMIN",font=("arial",12,"bold"),bg="cyan2",fg="red",bd=4)
        lbl_title.place(x=900,y=5,width=280,height=40)


        #**********************logo *************************
        img=Image.open(r"C:\Users\admin\Desktop\SE project\photos\jecrc logo.png")
        img=img.resize((90,45),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photosimg,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=45)

        #**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",20,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #**********************labels and entries*************************
        # floor
        lbl_floor=Label(labelframeleft,text="Floor: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room no
        lbl_roomNo=Label(labelframeleft,text="Room No: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomNo.grid(row=1,column=0,sticky=W,padx=20)

        self.var_RoomNo=StringVar()
        entry_roomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_roomNo.grid(row=1,column=1,sticky=W)

        # room type
        lbl_RoomType=Label(labelframeleft,text="Room Type: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_RoomType=StringVar()
        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_RoomType,width=20,state="readonly")
        combo_RoomType["value"]=("CHOOSE","SINGLE","COMBINED")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=2,column=1)

        #**********************btns*************************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #**********************Table Frame search system*************************
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",20,"bold"))
        Table_Frame.place(x=600,y=52,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.Room_Table=ttk.Treeview(Table_Frame,column=('Floor','RoomType','RoomNo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("Floor",text="Floor")
        self.Room_Table.heading("RoomType",text="RoomType")
        self.Room_Table.heading("RoomNo",text="RoomNo")

        self.Room_Table['show']='headings'

        self.Room_Table.column("Floor",width=120)
        self.Room_Table.column("RoomType",width=120)
        self.Room_Table.column("RoomNo",width=120)
        
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","Please fill all the fields.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_RoomNo.get()
                                                                                        
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success","New room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

# Fetching fata into the table from database  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_RoomType.set(row[1]),
        self.var_RoomNo.set(row[2])

# Update button
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_RoomNo.get()
                                                                                        ))
                                                                                                                                                                        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)
    
    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hostel Management System","Do you want to delete this room detail?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinjalmysql@28",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset function
    def reset(self):
        self.var_floor.set(""),
        self.var_RoomType.set(""),
        self.var_RoomNo.set("")


if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop() 