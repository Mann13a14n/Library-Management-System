from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Report")
        self.root.geometry("1293x568+230+220")


         # ================== Variable =======================

        self.var_Contact_No = StringVar()
        self.var_Student_Name = StringVar()
        self.var_Issu= StringVar()
        self.var_Shift_Type=StringVar()


        # ==================  Title  ========================

        lbl_title = Label(self.root,text="Complaint", font=("Calibri", 30, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 0, width= 1295, height=50)

         # ================== Logo Image  ========================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((80, 48), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=80, height=48)

         # ==================  Lable Frame  ========================

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Student_Details", font=("calibri", 20, "bold"), padx=2)
        labelframeleft.place(x=3, y=50, width=423, height=500)

        # ==================  Lables and Entry  ========================

        # == Contact_No ==
        lbl_contact_no= Label(labelframeleft,text="Contact No.",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_contact_no.grid(row=0, column=0,sticky=W)

        contact_no = ttk.Entry(labelframeleft,textvariable=self.var_Contact_No, width=33, font=("calibri", 12, "bold") )
        contact_no.grid(row=0, column=1)

        # == Student Name ==
        lbl_Student_Name= Label(labelframeleft,text="Student Name",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_Student_Name.grid(row=1, column=0,sticky=W)
        
        Student_Name = ttk.Entry(labelframeleft, textvariable=self.var_Student_Name , width=33, font=("calibri", 12, "bold"))
        Student_Name.grid(row=1, column=1)

        # == Issu ==
        lbl_Issu= Label(labelframeleft,text=" What's Complaint",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_Issu.grid(row=2, column=0,sticky=W)

        Issu = ttk.Entry(labelframeleft,textvariable=self.var_Issu, width=33, font=("calibri", 12, "bold"))
        Issu.grid(row=2, column=1, padx=5, ipady=40)


        # == Shift Type Combo Box ==
        lbl_Shift= Label(labelframeleft,text="Shift Type",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Shift.grid(row=3, column=0,sticky=W)

        box_Shift= ttk.Combobox(labelframeleft, textvariable=self.var_Shift_Type,font=("calibri",12), width=31, state="readonly")
        box_Shift["value"]= ("Day", "Night")
        box_Shift.grid(row=3, column=1)


        #============================ Button =================================
        btn_frame = Frame(labelframeleft,bd =2, relief=RIDGE)
        btn_frame.place(x=6, y=300, width=403, height=120)

        btn_Add = Button(btn_frame, text= "Add", command=self.add_data,  font=("calibri", 13, "bold"), bg= "green", fg="Black", width=20, cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=5,pady=9)

        btn_Update = Button(btn_frame, text="Update", command=self.update, font=("calibri", 13, "bold"), bg= "gray", fg="Black", width=20, cursor="hand2")
        btn_Update.grid(row=0, column=1, padx=5,pady=9)

        btn_Delete = Button(btn_frame, text="Delete", command=self.delete, font=("calibri", 13, "bold"), bg= "red", fg="Black", width=20, cursor="hand2")
        btn_Delete.grid(row=1, column=0, padx=5,pady=9)

        btn_Reset = Button(btn_frame, text="Reset", command=self.reset, font=("calibri", 13, "bold"), bg= "gray", fg="Black", width=20, cursor="hand2")
        btn_Reset.grid(row=1, column=1, padx=5,pady=9)

        #==================Search Table Frame ===============================

        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text=" Search and View Details", font=("calibri", 15, "bold"), padx=2, cursor="hand2")
        table_frame.place(x=435, y=50, width=860, height=515)


         # ====================== Show Book Record Table =================================

        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=6, width=800, height=450)

        scroll_x= ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Issu_Table= ttk.Treeview(details_table, columns=("Contact No", "Student Name", "Issu","Shift Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Issu_Table.xview)
        scroll_y.config(command=self.Issu_Table.yview)

        self.Issu_Table.heading("Contact No", text="Contact No.")
        self.Issu_Table.heading("Student Name", text="Student Name")
        self.Issu_Table.heading("Issu", text= "What's Complaint")
        self.Issu_Table.heading("Shift Type", text="Shift Type")

        self.Issu_Table["show"]= "headings"

        self.Issu_Table.column("Contact No", width= 60)
        self.Issu_Table.column("Student Name", width= 60)
        self.Issu_Table.column("Issu", width = 220)
        self.Issu_Table.column("Shift Type", width= 50)       


        self.Issu_Table.pack(fill=BOTH, expand=1)
        self.Issu_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Contact_No.get()=="" or self.var_Student_Name.get()=="":
            messagebox.showerror("Error", "All Entry are required", parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Issu values(%s,%s,%s,%s)",(
                                                                                    self.var_Contact_No.get(),
                                                                                    self.var_Student_Name.get(),
                                                                                    self.var_Issu.get(),
                                                                                    self.var_Shift_Type.get()

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Your Issu has been added",parent= self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Issu")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Issu_Table.delete(*self.Issu_Table.get_children())
            for i in rows:
                self.Issu_Table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row= self.Issu_Table.focus()
        content= self.Issu_Table.item(cursor_row)
        row= content["values"]

        self.var_Contact_No.set(row[0]),
        self.var_Student_Name.set(row[1]),
        self.var_Issu.set(row[2]),
        self.var_Shift_Type.set(row[3])



    def update(self):
        if self.var_Contact_No.get()=="":
            messagebox.showerror("Enter", "Please Enter Seat Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()                                                                                                                          
            my_cursor.execute("update Issu set Student_Name=%s, Issues=%s,Shift_Type=%s where Contact_No=%s",(
                                                                                     self.var_Student_Name.get(),
                                                                                     self.var_Issu.get(),
                                                                                     self.var_Shift_Type.get(),
                                                                                     self.var_Contact_No.get()   

                                                                                 ))   
            conn.commit()
            self.fetch_data()
            conn.close()                                                             
            messagebox.showinfo("Update","Your Issu has been updated successfully",parent=self.root)


    def delete(self):
        smsdelete = messagebox.askyesno("Library_Management_System", "Do you want to delete this Issu",parent=self.root)
        if smsdelete>0:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()
            query = "delete from Issu where Contact_No=%s"
            value =(self.var_Contact_No.get(),)
            my_cursor.execute(query,value)
        else:
            if not self.delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Contact_No.set(""),
        self.var_Student_Name.set(""),
        self.var_Issu.set(""),
        self.var_Shift_Type.set("")







if __name__ == "__main__":
    root=Tk()
    obj= Report(root)
    root.mainloop()