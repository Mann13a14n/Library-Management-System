from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Seat_Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Seat Details")
        self.root.geometry("1295x568+230+220")

        # ================= variable =======================

        self.var_contact_no = StringVar()
        self.var_row_no = StringVar()
        self.var_registration_date = StringVar()
        self.var_in_time = StringVar()
        self.var_out_time = StringVar()
        self.var_available_seat = StringVar()
        self.var_shift_type = StringVar()
        self.var_coffee = StringVar()
        self.var_coffee_charge = IntVar()
        self.var_fee_amount = IntVar()
        self.var_total_amount =StringVar()


        # ==================  Title  ========================

        lbl_title = Label(self.root,text="SEAT REGISTRATION DETAILS", font=("Calibri", 30, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 0, width= 1295, height=50)

         # ================== Logo Image  ========================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((80, 48), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=80, height=48)

         # ==================  Lable Frame  ========================

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Registration_Details", font=("calibri", 18, "bold"), padx=2)
        labelframeleft.place(x=3, y=50, width=423, height=515)


        # ==================  Lables and Entry  ========================
        # == Contact_No ==
        lbl_contact_no= Label(labelframeleft,text="Contact No.",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_contact_no.grid(row=0, column=0,sticky=W)
        
        enty_contact_no = ttk.Entry(labelframeleft, textvariable=self.var_contact_no,width=22, font=("calibri", 12, "bold") )
        enty_contact_no.grid(row=0, column=1,sticky=W)

        # === Get Details ===

        btn_get_data = Button(labelframeleft, text= "Get Details", command=self.fetch_contact,font=("calibri", 11, "bold"), bg= "gray", fg="Black", width=10)
        btn_get_data.place(x=320 , y=3)


        # ==Row_No ==
        lbl_row_no= Label(labelframeleft,text="Seat Row No.",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_row_no.grid(row=1, column=0,sticky=W)

        row_no = ttk.Combobox(labelframeleft, textvariable=self.var_row_no,width=33, font=("calibri", 12, "bold"), state="readonly" )
        row_no["value"]= ("A","B","C","D","E","F","G")
        row_no.grid(row=1, column=1)

        # == Registration_date ==
        lbl_stu_reg_date= Label(labelframeleft,text="Registration Date",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_stu_reg_date.grid(row=2, column=0,sticky=W)
        
        enty_reg_date = ttk.Entry(labelframeleft, textvariable=self.var_registration_date,width=35, font=("calibri", 12, "bold") )
        enty_reg_date.grid(row=2, column=1)

        # == In_Time ==
        lbl_stu_in_time= Label(labelframeleft,text=" In Time",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_stu_in_time.grid(row=3, column=0,sticky=W)
        
        in_time = ttk.Combobox(labelframeleft,textvariable=self.var_in_time,width=15, font=("calibri", 12, "bold"), state="readonly")
        in_time["value"]= ("6 am","8 am","10 am","12 pm","2 pm","4 pm","6 pm","8 pm","10 pm")
        in_time.place(x=127, y= 110)

        # == Out_Time ==
        lbl_stu_out_time= Label(labelframeleft,text="Out Time",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_stu_out_time.grid(row=4, column=0,sticky=W)
        
        out_time = ttk.Combobox(labelframeleft, textvariable=self.var_out_time,width=15,font=("calibri", 12, "bold"), state="readonly")
        out_time["value"]= ("6 am","8 am","10 am","12 pm","2 pm","4 pm","6 pm","8 pm","10 pm")
        out_time.place(x=127, y=145)

        # == Available_Seats ==
        
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select Seat_No from Seat_Details")
        rows1=my_cursor.fetchall()


        lbl_available_Seat= Label(labelframeleft,text="Seat_No",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_available_Seat.grid(row=5, column=0,sticky=W)
        
        available_Seat = ttk.Combobox(labelframeleft, textvariable=self.var_available_seat,width=33, font=("calibri", 12, "bold"),state="readonly")
        available_Seat["value"]= rows1
        available_Seat.grid(row=5, column=1)

         # == Shift ==
        lbl_shift= Label(labelframeleft,text="Shift Type",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_shift.grid(row=6, column=0,sticky=W)
        
        shift_type= ttk.Combobox(labelframeleft, textvariable=self.var_shift_type,font=("calibri",12), width=33, state="readonly")
        shift_type["value"]= ("Day","Night")
        shift_type.grid(row=6, column=1)


        # == coffee ==
        lbl_coffee= Label(labelframeleft,text="Count of Coffee",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_coffee.grid(row=7, column=0,sticky=W)

        NoOfCoffee= ttk.Combobox(labelframeleft, textvariable=self.var_coffee,font=("calibri",12), width=33, state="readonly")
        NoOfCoffee["value"]= (1,2,3,4)
        NoOfCoffee.grid(row=7, column=1)
        
               
        # == Coffee Charges ==
        lbl_Coffee_charge= Label(labelframeleft,text="Coffee Charge",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_Coffee_charge.grid(row=8, column=0,sticky=W)
        
        Coffee_charge = ttk.Combobox(labelframeleft, textvariable=self.var_coffee_charge,width=33, font=("calibri", 12, "bold"),state="readonly" )
        Coffee_charge["value"]=(30,50,80,100)
        Coffee_charge.grid(row=8, column=1)

        # == Fee Amount_amount ==
        lbl_fee_amount= Label(labelframeleft,text="Fee Amount",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_fee_amount.grid(row=9, column=0,sticky=W)
        
        fee_amount = ttk.Combobox(labelframeleft,textvariable=self.var_fee_amount,width=33, font=("calibri", 12, "bold"),state="readonly" )
        fee_amount["value"]= (800,1400)
        fee_amount.current(0)
        fee_amount.grid(row=9, column=1)

         # == Total Amount ==
        lbl_total_amount= Label(labelframeleft,text="Total Amount",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_total_amount.grid(row=10, column=0,sticky=W)
        
        enty_total_amount = ttk.Entry(labelframeleft, textvariable=self.var_total_amount,width=35, font=("calibri", 12, "bold"), state="readonly" )
        enty_total_amount.grid(row=10, column=1)


        #============================ Button =================================
        btn_frame = Frame(labelframeleft,bd =2, relief=RIDGE)
        btn_frame.place(x=0, y=395, width=415, height=85)

        btn_Add = Button(btn_frame, text= "Add", command=self.add_data,font=("calibri", 12, "bold"), bg= "green", fg="Black", width=12, cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=14, pady=3)

        btn_Update = Button(btn_frame, text="Update", command=self.update,font=("calibri", 12, "bold"), bg= "gray", fg="Black", width=12, cursor="hand2")
        btn_Update.grid(row=0, column=1, padx=14, pady=3)

        btn_Delete = Button(btn_frame, text="Delete", command=self.delete,font=("calibri", 12, "bold"), bg= "red", fg="Black", width=12, cursor="hand2")
        btn_Delete.grid(row=0, column=2, padx=14, pady=3)

        btn_Reset = Button(btn_frame, text="Reset", command=self.reset,font=("calibri", 12, "bold"), bg= "gray", fg="Black", width=12, cursor="hand2")
        btn_Reset.grid(row=1, column=0, padx=14, pady=5)

        btn_bill = Button(btn_frame, text= "Bill", command=self.bill,font=("calibri", 12, "bold"), bg= "gray", fg="Black", width=12, cursor="hand2")
        btn_bill.grid(row=1, column=2, padx=14, pady=5)



        #==================Search Table Frame ===============================

        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text=" Search and View Details", font=("calibri", 15, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lbl_searchBY= Label(table_frame,text="Search By",font=("Calibri", 12, "bold"), bg="yellow", fg="black")
        lbl_searchBY.grid(row=0, column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        DropDwon_search= ttk.Combobox(table_frame, textvariable=self.search_var,font=("calibri",12), width=20, state="readonly")
        DropDwon_search["value"]= ("Row_No","Contact_No", "Seat_No")
        DropDwon_search.grid(row=0, column=1, padx=2)

        self.text_search=StringVar()
        enty_search = ttk.Entry(table_frame, textvariable=self.text_search,width=24, font=("calibri", 12))
        enty_search.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, text="Search",command=self.search, font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9, cursor="hand2")
        btn_search.grid(row=0, column=3, padx=2)

        btn_showAll = Button(table_frame, text="Show All",command=self.fetch_data,font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9, cursor="hand2")
        btn_showAll.grid(row=0, column=4, padx=2)

        
        # ====================== Show Data Table =================================

        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=191)

        scroll_x= ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Seat_Table= ttk.Treeview(details_table, columns=("Contact", "Row","Date","In Time", "Out Time",
                                            "available","shift","coffee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Seat_Table.xview)
        scroll_y.config(command=self.Seat_Table.yview)

        self.Seat_Table.heading("Contact", text="Contact No.")
        self.Seat_Table.heading("Row", text="Seat Row No.")
        self.Seat_Table.heading("Date", text="Reg. Date")
        self.Seat_Table.heading("In Time", text="In-Time")
        self.Seat_Table.heading("Out Time", text="Out-Time")
        self.Seat_Table.heading("available", text="Seat No.")
        self.Seat_Table.heading("shift", text="Shift Type")
        self.Seat_Table.heading("coffee", text="Count of Coffee")
       # self.Seat_Table.heading("total fees", text="Total Fees")

        self.Seat_Table["show"]= "headings"

        self.Seat_Table.column("Contact", width= 70)
        self.Seat_Table.column("Row", width= 60)
        self.Seat_Table.column("Date", width= 100)
        self.Seat_Table.column("In Time", width= 60)
        self.Seat_Table.column("Out Time", width= 60)
        self.Seat_Table.column("available", width= 80)
        self.Seat_Table.column("shift", width= 60)
        self.Seat_Table.column("coffee", width= 50)
       # self.Seat_Table.column("total fees", width= 50)

        
        self.Seat_Table.pack(fill=BOTH, expand=1)

        self.Seat_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    #== Add Data ===

    def add_data(self):
        if self.var_contact_no.get()=="" or self.var_in_time.get()=="":
            messagebox.showerror("Error", "All Entry are required")
        else:
            try:
                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Seat_allotment values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact_no.get(),
                                                                                    self.var_row_no.get(),
                                                                                    self.var_registration_date.get(),
                                                                                    self.var_in_time.get(),
                                                                                    self.var_out_time.get(),
                                                                                    self.var_available_seat.get(),
                                                                                    self.var_shift_type.get(),
                                                                                    self.var_coffee.get()
                                                                                   # self. var_total_amount()
                                                                                                                                                      
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Seat Allotment Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es)}",parent=self.root)
    
    #=== Fetch_data ====
    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Seat_allotment")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Seat_Table.delete(*self.Seat_Table.get_children())
            for i in rows:
                self.Seat_Table.insert("",END,values=i)
            conn.commit()
            conn.close()

        # ==== Get Cursor ====

    def get_cursor(self,event=""):
        cursor_row= self.Seat_Table.focus()
        content= self.Seat_Table.item(cursor_row)
        row= content["values"]

        self.var_contact_no.set(row[0]),
        self.var_row_no.set(row[1]),
        self.var_registration_date.set(row[2]),
        self.var_in_time.set(row[3]),
        self.var_out_time.set(row[4]),
        self.var_available_seat.set(row[5]),
        self.var_shift_type.set(row[6]),
        self.var_coffee.set(row[7])
      #  self.var_total_amount.set(row[8])    

    # == Update Function ==
    def update(self):
        if self.var_contact_no.get()=="":
            messagebox.showerror("Enter", "Please Enter Contact Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()                                                                                                                          
            my_cursor.execute("update Seat_allotment set Row_No=%s,Registration_date=%s, In_Time=%s,Out_Time=%s, Seat_No=%s, Shift_Type=%s, COffee=%s  where Contact_No=%s",(
                                                                                                                                                                                        
                                                                                                                                                                                    self.var_row_no.get(),
                                                                                                                                                                                    self.var_registration_date.get(),
                                                                                                                                                                                    self.var_in_time.get(),
                                                                                                                                                                                    self.var_out_time.get(),
                                                                                                                                                                                    self.var_available_seat.get(),
                                                                                                                                                                                    self.var_shift_type.get(),
                                                                                                                                                                                    self.var_coffee.get(),
                                                                                                                                                                                    self.var_contact_no.get()
                                                                                                                                                                                      
                                                                                                                                                                                 ))   
            conn.commit()
            self.fetch_data()
            conn.close()                                                             
            messagebox.showinfo("Update","Seat Allotment Details has been updated successfully",parent=self.root)
   
  
    #== Detele Function ==
  
    def delete(self):
        smsdelete = messagebox.askyesno("Library_Management_System", "Do you want to delete this Seat allotment",parent=self.root)
        if smsdelete>0:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()
            query = "delete from Seat_allotment where Contact_No=%s"
            value =(self.var_contact_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #== Rest Function ===

    def reset(self):
        self.var_row_no.set(""),
        self.var_registration_date.set(""),
        self.var_in_time.set(""),
        self.var_out_time.set(""),
        self.var_available_seat.set(""),
        self.var_shift_type.set(""),
        self.var_coffee.set(""),
        self.var_contact_no.set(""),
        self.var_coffee_charge.set("")
        self.var_fee_amount.set("")
      #  self.var_total_amount.set("")

    # == Total Amount ==
    def bill(self):

            try:
                coffee_amount = self.var_coffee_charge.get()
                fee_amount = self.var_fee_amount.get()

                total_amount = coffee_amount + fee_amount

                self.var_total_amount.set(total_amount)

            except Exception as e:
                 messagebox.showerror("Error", f"An error occurred while calculating the total: {int(e)}", parent=self.root)

    

    #== Search BY===

    def search(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()

        query = "SELECT * FROM Seat_allotment WHERE " + self.search_var.get() + " LIKE %s"
        search_term = "%" + self.text_search.get() + "%"

        my_cursor.execute(query, (search_term,))
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.Seat_Table.delete(*self.Seat_Table.get_children())
            for i in rows:
                self.Seat_Table.insert("",END,values=i)
            conn.commit()
        conn.close()



        

#==================== Show Data ==================================
    def fetch_contact(self):
        if self.var_contact_no.get()=="":
            messagebox.showerror("Error","Please enter Contact Number", parent=self.root)
        else:
             conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
             my_cursor=conn.cursor()
             query = (" Select Student_Name from Student_Details Where Contact_Number=%s")
             value=(self.var_contact_no.get(),)
             my_cursor.execute(query,value)
             row= my_cursor.fetchone()

             if row==None:
                messagebox.showerror("Error", "This Contact Number not found", parent=self.root)
             else:
                conn.commit()
                conn.close()

                shwoDataframe = LabelFrame(self.root,text="Student_Details",font=("calibri", 15, "bold"), bd=4, relief=RIDGE, padx=2)
                shwoDataframe.place(x=455, y= 55, width=800, height=210)
                

                # === Student_ Name ====
                lblName= Label(shwoDataframe, text="Name:", font=("calibri", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl1 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl1.place(x=120, y=0)

                #==== Father's Name =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Fathers_Name from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblFather= Label(shwoDataframe, text="Father's Name:", font=("calibri", 12, "bold"))
                lblFather.place(x=350, y=0)

                lbl2 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl2.place(x=520, y=0)

                #==== Gender =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Gender from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblGender= Label(shwoDataframe, text="Gender:", font=("calibri", 12, "bold"))
                lblGender.place(x=0, y=40)

                lbl3 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl3.place(x=120, y=40)

                #==== Email_Id =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Email_Id from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblEamil_id= Label(shwoDataframe, text="Email-Id:", font=("calibri", 12, "bold"))
                lblEamil_id.place(x=350, y=40)

                lbl4 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl4.place(x=520, y=40)

                #==== Address =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Address from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblAddress= Label(shwoDataframe, text="Address:", font=("calibri", 12, "bold"))
                lblAddress.place(x=0, y=80)

                lbl5 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl5.place(x=120, y=80)

                #==== Student_Id =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Student_Id from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblStudent_Id= Label(shwoDataframe, text="Student Id Type:", font=("calibri", 12, "bold"))
                lblStudent_Id.place(x=350, y=80)

                lbl6 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl6.place(x=520, y=80)


                #==== Country =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Nationality from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblNationality= Label(shwoDataframe, text="Country:", font=("calibri", 12, "bold"))
                lblNationality.place(x=0, y=120)

                lbl7 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl7.place(x=120, y=120)

                #==== Id_Number =======

                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                query = ("Select Id_Number from Student_Details Where Contact_Number=%s")
                value=(self.var_contact_no.get(),)
                my_cursor.execute(query,value)
                row= my_cursor.fetchone()

                lblId_Number= Label(shwoDataframe, text="Id Number:", font=("calibri", 12, "bold"))
                lblId_Number.place(x=350, y=120)

                lbl8 = Label(shwoDataframe, text=row, font= ("calibri", 12, "bold"))
                lbl8.place(x=520, y=120)






if __name__ == "__main__":
    root=Tk()
    obj=Seat_Registration(root)
    root.mainloop()