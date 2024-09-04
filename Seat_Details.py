from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Books Record")
        self.root.geometry("1293x568+230+220")


         # ================== Variable =======================

        self.var_Seat_Row_No = StringVar()
        self.var_Seat_No= StringVar()
        self.var_Shift_Type=StringVar()


        # ==================  Title  ========================

        lbl_title = Label(self.root,text="SEAT DETAILS", font=("Calibri", 30, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 0, width= 1295, height=50)

         # ================== Logo Image  ========================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((80, 48), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=80, height=48)

         # ==================  Lable Frame  ========================

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Seat_Details", font=("calibri", 20, "bold"), padx=2)
        labelframeleft.place(x=3, y=50, width=423, height=370)

        # ==================  Lables and Entry  ========================

        # == Seat Row_No ==
        lbl_row_no= Label(labelframeleft,text="Seat Row No.",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_row_no.grid(row=0, column=0,sticky=W)

        row_no = ttk.Combobox(labelframeleft,textvariable=self.var_Seat_Row_No, width=33, font=("calibri", 12, "bold"), state="readonly" )
        row_no["value"]= ("A","B","C","D","E","F","G")
        row_no.grid(row=0, column=1)

        # == Seat Number ==
        lbl_Column_no= Label(labelframeleft,text="Seat_No",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_Column_no.grid(row=1, column=0,sticky=W)
        
        Column_No = ttk.Entry(labelframeleft, textvariable=self.var_Seat_No , width=35, font=("calibri", 12, "bold"))
        Column_No.grid(row=1, column=1)

        # == Shift Type Combo Box ==
        lbl_Shift= Label(labelframeleft,text="Shift Type",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Shift.grid(row=2, column=0,sticky=W)

        box_Shift= ttk.Combobox(labelframeleft, textvariable=self.var_Shift_Type,font=("calibri",12), width=33, state="readonly")
        box_Shift["value"]= ("Day", "Night")
        box_Shift.grid(row=2, column=1)


        #============================ Button =================================
        btn_frame = Frame(labelframeleft,bd =2, relief=RIDGE)
        btn_frame.place(x=6, y=200, width=403, height=120)

        btn_Add = Button(btn_frame, text= "Add", command=self.add_data, font=("calibri", 13, "bold"), bg= "green", fg="Black", width=20, cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=5,pady=9)

        btn_Update = Button(btn_frame, text="Update", command=self.update,font=("calibri", 13, "bold"), bg= "gray", fg="Black", width=20, cursor="hand2")
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
        details_table.place(x=0, y=6, width=500, height=350)

        scroll_x= ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Seat_Details_Table= ttk.Treeview(details_table, columns=("Seat Row No", "Seat No","Shift Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Seat_Details_Table.xview)
        scroll_y.config(command=self.Seat_Details_Table.yview)

        self.Seat_Details_Table.heading("Seat Row No", text="Seat Row No.")
        self.Seat_Details_Table.heading("Seat No", text="Seat No.")
        self.Seat_Details_Table.heading("Shift Type", text="Shift Type")

        self.Seat_Details_Table["show"]= "headings"

        self.Seat_Details_Table.column("Seat Row No", width= 80)
        self.Seat_Details_Table.column("Seat No", width= 80)
        self.Seat_Details_Table.column("Shift Type", width= 80)       


        self.Seat_Details_Table.pack(fill=BOTH, expand=1)
        self.Seat_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Seat_Row_No.get()=="" or self.var_Seat_No.get()=="":
            messagebox.showerror("Error", "All Entry are required")
        else:
            try:
                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Seat_Details values(%s,%s,%s)",(
                                                                                    self.var_Seat_Row_No.get(),
                                                                                    self.var_Seat_No.get(),
                                                                                    self.var_Shift_Type.get(),

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Seat Details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Seat_Details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Seat_Details_Table.delete(*self.Seat_Details_Table.get_children())
            for i in rows:
                self.Seat_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row= self.Seat_Details_Table.focus()
        content= self.Seat_Details_Table.item(cursor_row)
        row= content["values"]

        self.var_Seat_Row_No.set(row[0]),
        self.var_Seat_No.set(row[1]),
        self.var_Shift_Type.set(row[2])



    def update(self):
        if self.var_Seat_No.get()=="":
            messagebox.showerror("Enter", "Please Enter Seat Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()                                                                                                                          
            my_cursor.execute("update Seat_Details set Seat_Row_No=%s,Shift_Type=%s where Seat_No=%s",(
                                                                                     self.var_Seat_Row_No.get(),
                                                                                     self.var_Shift_Type.get(),
                                                                                     self.var_Seat_No.get()   

                                                                                 ))   
            conn.commit()
            self.fetch_data()
            conn.close()                                                             
            messagebox.showinfo("Update","Seat Details has been updated successfully",parent=self.root)


    def delete(self):
        smsdelete = messagebox.askyesno("Library_Management_System", "Do you want to delete this Seat Details",parent=self.root)
        if smsdelete>0:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()
            query = "delete from Seat_Details where Seat_No=%s"
            value =(self.var_Seat_No.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Seat_Row_No.set(""),
        self.var_Seat_No.set(""),
        self.var_Shift_Type.set("")







if __name__ == "__main__":
    root=Tk()
    obj= Details(root)
    root.mainloop()