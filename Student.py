from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Stu_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.root.geometry("1295x568+230+220")

        # ================== Variable =======================

        self.var_Ref_No=StringVar()
        x= random.randint(100,999)
        self.var_Ref_No.set(str(x))

        self.var_Student_Name= StringVar()
        self.var_Fathers_Name=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact_Number=StringVar()
        self.var_Email_Id=StringVar()
        self.var_Address=StringVar()
        self.var_Student_Id=StringVar()
        self.var_Id_Number=StringVar()
        self.var_Nationality=StringVar()

        # ==================  Title  ========================

        lbl_title = Label(self.root,text="ADD STUDENT DETAILS", font=("Calibri", 30, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 0, width= 1295, height=50)

         # ================== Logo Image  ========================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((80, 48), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=80, height=48)

         # ==================  Lable Frame  ========================

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Student_Details", font=("calibri", 20, "bold"), padx=2)
        labelframeleft.place(x=3, y=50, width=423, height=515)

        # ==================  Lables and Entry  ========================
        # == Stu_ref ==
        lbl_stu_ref= Label(labelframeleft,text="Ref No",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_stu_ref.grid(row=0, column=0,sticky=W)
        
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_Ref_No,width=35, font=("calibri", 12, "bold"), state="readonly")
        enty_ref.grid(row=0, column=1)

        # == Stu_name ==
        lbl_stu_name= Label(labelframeleft,text="Student Name",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_stu_name.grid(row=1, column=0,sticky=W)
        
        enty_name = ttk.Entry(labelframeleft,textvariable=self.var_Student_Name,width=35, font=("calibri", 12,))
        enty_name.grid(row=1, column=1)

        # == Father's Name ==
        lbl_stu_father= Label(labelframeleft,text="Father's Name",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_stu_father.grid(row=2, column=0,sticky=W)
        
        enty_father = ttk.Entry(labelframeleft,textvariable=self.var_Fathers_Name,width=35, font=("calibri", 12))
        enty_father.grid(row=2, column=1)

        # == Gender Combo Box ==
        lbl_gender= Label(labelframeleft,text="Gender",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_gender.grid(row=3, column=0,sticky=W)

        box_gender= ttk.Combobox(labelframeleft, textvariable=self.var_Gender,font=("calibri",12), width=33, state="readonly")
        box_gender["value"]= ("Male", "Female", "Other")
        box_gender.grid(row=3, column=1)

        # == Contact Number ==
        lbl_contact= Label(labelframeleft,text="Contact Number",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_contact.grid(row=4, column=0,sticky=W)
        
        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_Contact_Number,width=35, font=("calibri", 12))
        enty_contact.grid(row=4, column=1)

        # == Email_id ==
        lbl_email= Label(labelframeleft,text="Email_Id",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_email.grid(row=5, column=0,sticky=W)
        
        enty_email = ttk.Entry(labelframeleft, textvariable=self.var_Email_Id,width=35, font=("calibri", 12))
        enty_email.grid(row=5, column=1)

        # == Address ==
        lbl_address= Label(labelframeleft,text="Address",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_address.grid(row=6, column=0,sticky=W)
        
        enty_address = ttk.Entry(labelframeleft, textvariable=self.var_Address,width=35, font=("calibri", 12,))
        enty_address.grid(row=6, column=1)

        # == Student_ID Combo Box==
        lbl_id_type= Label(labelframeleft,text="Student_Id",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_id_type.grid(row=7, column=0,sticky=W)

        box_type= ttk.Combobox(labelframeleft, textvariable=self.var_Student_Id,font=("calibri",12), width=33, state="readonly")
        box_type["value"]= ("Aadhar Card", "Pan Card", "Driving Licence" ,"Other")
        box_type.grid(row=7, column=1)


        # == ID Numbar ==
        lbl_id= Label(labelframeleft,text="Id_Number",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_id.grid(row=8, column=0,sticky=W)
        
        id_number = ttk.Entry(labelframeleft, textvariable=self.var_Id_Number,width=35, font=("calibri", 12 ))
        id_number.grid(row=8, column=1)

        # == Nationality Combo Box ==
        lbl_nationality= Label(labelframeleft,text="Nationality",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_nationality.grid(row=9, column=0,sticky=W)

        box_nationality= ttk.Combobox(labelframeleft, textvariable=self.var_Nationality,font=("calibri",12), width=33, state="readonly")
        box_nationality["value"]= ("Indian","Other")
        box_nationality.grid(row=9, column=1)

        #============================ Button =================================
        btn_frame = Frame(labelframeleft,bd =2, relief=RIDGE)
        btn_frame.place(x=0, y=410, width=419, height=38)

        btn_Add = Button(btn_frame, text= "Add",command=self.add_data,font=("calibri", 12, "bold"), bg= "green", fg="Black", width=10, cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=2)

        btn_Update = Button(btn_frame, text="Update", command=self.update,font=("calibri", 12, "bold"), bg= "gray", fg="Black", width=12, cursor="hand2")
        btn_Update.grid(row=0, column=1, padx=2)

        btn_Delete = Button(btn_frame, text="Delete", command=self.delete,font=("calibri", 12, "bold"), bg= "red", fg="Black", width=12, cursor="hand2")
        btn_Delete.grid(row=0, column=2, padx=2)

        btn_Reset = Button(btn_frame, text="Reset",command=self.reset,font=("calibri", 12, "bold"), bg= "gray", fg="Black", width=11, cursor="hand2")
        btn_Reset.grid(row=0, column=3, padx=2)

        #==================Search Table Frame ===============================

        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text=" Search and View Details", font=("calibri", 15, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=515)

        lbl_searchBY= Label(table_frame,text="Search By",font=("Calibri", 12, "bold"), bg="yellow", fg="black")
        lbl_searchBY.grid(row=0, column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        DropDwon_search= ttk.Combobox(table_frame, textvariable=self.search_var,font=("calibri",12), width=20, state="readonly")
        DropDwon_search["value"]= ("Ref_No","Student_Name","Contact_Number")
        DropDwon_search.grid(row=0, column=1, padx=2)

        self.text_search=StringVar()
        enty_search = ttk.Entry(table_frame, textvariable=self.text_search,width=24, font=("calibri", 12))
        enty_search.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, text="Search", command=self.search,font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9)
        btn_search.grid(row=0, column=3, padx=2)

        btn_showAll = Button(table_frame, text="Show All",command=self.fetch_data,font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9)
        btn_showAll.grid(row=0, column=4, padx=2)

        # ====================== Show Data Table =================================

        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x= ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Stu_Details_Table= ttk.Treeview(details_table, columns=("Ref No", "Name","Father","Gender", "Contact_No.",
                                            "Email_Id","Address","Id_Type", "Id_Number","Nationality"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Stu_Details_Table.xview)
        scroll_y.config(command=self.Stu_Details_Table.yview)

        self.Stu_Details_Table.heading("Ref No", text="Ref. No.")
        self.Stu_Details_Table.heading("Name", text="Student_Name")
        self.Stu_Details_Table.heading("Father", text="Father's Name")
        self.Stu_Details_Table.heading("Gender", text="Gender")
        self.Stu_Details_Table.heading("Contact_No.", text="Contact_No.")
        self.Stu_Details_Table.heading("Email_Id", text="Email_Id")
        self.Stu_Details_Table.heading("Address", text="Address")
        self.Stu_Details_Table.heading("Id_Type", text="Id_Type")
        self.Stu_Details_Table.heading("Id_Number", text="Id_Number")
        self.Stu_Details_Table.heading("Nationality", text="Nationality")

        self.Stu_Details_Table["show"]= "headings"

        self.Stu_Details_Table.column("Ref No", width= 70)
        self.Stu_Details_Table.column("Name", width= 100)
        self.Stu_Details_Table.column("Father", width= 120)
        self.Stu_Details_Table.column("Gender", width= 50)
        self.Stu_Details_Table.column("Contact_No.", width= 100)
        self.Stu_Details_Table.column("Email_Id", width= 120)
        self.Stu_Details_Table.column("Address", width= 100)
        self.Stu_Details_Table.column("Id_Type", width= 70)
        self.Stu_Details_Table.column("Id_Number", width= 100)
        self.Stu_Details_Table.column("Nationality", width= 70)
        


        self.Stu_Details_Table.pack(fill=BOTH, expand=1)
        self.Stu_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Contact_Number.get()=="" or self.var_Fathers_Name.get()=="":
            messagebox.showerror("Error", "All Entry are required")
        else:
            try:
                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_Ref_No.get(),
                                                                                    self.var_Student_Name.get(),
                                                                                    self.var_Fathers_Name.get(),
                                                                                    self.var_Gender.get(),
                                                                                    self.var_Contact_Number.get(),
                                                                                    self.var_Email_Id.get(),
                                                                                    self.var_Address.get(),
                                                                                    self.var_Student_Id.get(),
                                                                                    self.var_Id_Number.get(),
                                                                                    self.var_Nationality.get()                                                                                                                                                         
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Student_Details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_children())
            for i in rows:
                self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row= self.Stu_Details_Table.focus()
        content= self.Stu_Details_Table.item(cursor_row)
        row= content["values"]

        self.var_Ref_No.set(row[0]),
        self.var_Student_Name.set(row[1]),
        self.var_Fathers_Name.set(row[2]),
        self.var_Gender.set(row[3]),
        self.var_Contact_Number.set(row[4]),
        self.var_Email_Id.set(row[5]),
        self.var_Address.set(row[6]),
        self.var_Student_Id.set(row[7]),
        self.var_Id_Number.set(row[8]),
        self.var_Nationality.set(row[9])             


    def update(self):
        if self.var_Contact_Number.get()=="":
            messagebox.showerror("Enter", "Please Enter Contact Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()                                                                                                                          
            my_cursor.execute("update Student_Details set Student_Name=%s,Fathers_Name=%s, Gender=%s,Contact_Number=%s, Email_Id=%s, Address=%s, Student_Id=%s, Id_Number=%s,Nationality=%s where Ref_No=%s",(
                                                                                                                                                                                                        self.var_Student_Name.get(),
                                                                                                                                                                                                        self.var_Fathers_Name.get(),
                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                        self.var_Contact_Number.get(),
                                                                                                                                                                                                        self.var_Email_Id.get(),
                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                        self.var_Student_Id.get(),
                                                                                                                                                                                                        self.var_Id_Number.get(),
                                                                                                                                                                                                        self.var_Nationality.get(),
                                                                                                                                                                                                        self.var_Ref_No.get()   

                                                                                                                                                                                                   ))   
            conn.commit()
            self.fetch_data()
            conn.close()                                                             
            messagebox.showinfo("Update","Student Details has been updated successfully",parent=self.root)


    def delete(self):
        smsdelete = messagebox.askyesno("Library_Management_System", "Do you want to delete this Student Details",parent=self.root)
        if smsdelete>0:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()
            query = "delete from Student_Details where Ref_No=%s"
            value =(self.var_Ref_No.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Ref_No.set(""),
        self.var_Student_Name.set(""),
        self.var_Fathers_Name.set(""),
        self.var_Gender.set(""),
        self.var_Contact_Number.set(""),
        self.var_Email_Id.set(""),
        self.var_Address.set(""),
        self.var_Student_Id.set(""),
        self.var_Id_Number.set(""),
        self.var_Nationality.set("")

        x= random.randint(100,9999)
        self.var_Ref_No.set(str(x))


    #== Search By===
    def search(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()

        query = "SELECT * FROM Student_Details WHERE " + self.search_var.get() + " LIKE %s"
        search_term = "%" + self.text_search.get() + "%"

        my_cursor.execute(query, (search_term,))
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.Stu_Details_Table.delete(*self.Stu_Details_Table.get_children())
            for i in rows:
                self.Stu_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()





if __name__ == "__main__":
    root=Tk()
    obj=Stu_Win(root)
    root.mainloop()
