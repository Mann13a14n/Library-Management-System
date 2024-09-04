from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Books_Record:
    def __init__(self, root):
        self.root = root
        self.root.title("Books Record")
        self.root.geometry("1295x568+230+220")

        # ================== Variable =======================

        self.var_Serial_No=StringVar()
        x= random.randint(1,499)
        self.var_Serial_No.set(str(x))

        self.var_Book_Name= StringVar()
        self.var_Writers_Name=StringVar()
        self.var_Row_No=StringVar()
        self.var_Column_No=StringVar()
        self.var_Language=StringVar()
        self.var_Stu_Ref_No=StringVar()
        self.var_Stu_Name=StringVar()
        
        # ==================  Title  ========================

        lbl_title = Label(self.root,text="ADD BOOK RECORDS", font=("Calibri", 30, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 0, width= 1295, height=50)

         # ================== Logo Image  ========================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((80, 48), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=80, height=48)

         # ==================  Lable Frame  ========================

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Book_Details", font=("calibri", 20, "bold"), padx=2)
        labelframeleft.place(x=3, y=50, width=423, height=515)

        # ==================  Lables and Entry  ========================
        # == Book Serial No. ==
        lbl_Book_Serial= Label(labelframeleft,text="Book Serial No.",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Book_Serial.grid(row=0, column=0,sticky=W)
        
        enty_Book_Serial = ttk.Entry(labelframeleft,textvariable=self.var_Serial_No,width=35, font=("calibri", 12, "bold"), state="readonly")
        enty_Book_Serial.grid(row=0, column=1)

        # == Book_name ==
        lbl_Book_name= Label(labelframeleft,text="Book Name",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Book_name.grid(row=1, column=0,sticky=W)
        
        enty_Book_name = ttk.Entry(labelframeleft,textvariable=self.var_Book_Name,width=35, font=("calibri", 12,))
        enty_Book_name.grid(row=1, column=1)

        # == Book's Writer ==
        lbl_Books_writer= Label(labelframeleft,text=" Book's Writer",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Books_writer.grid(row=2, column=0,sticky=W)
        
        enty_writer = ttk.Entry(labelframeleft,textvariable=self.var_Writers_Name,width=35, font=("calibri", 12))
        enty_writer.grid(row=2, column=1)

         # ==Row_No ==
        lbl_row_no= Label(labelframeleft,text="Book Row No.",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_row_no.grid(row=3, column=0,sticky=W)

        row_no = ttk.Combobox(labelframeleft, textvariable=self.var_Row_No,width=33, font=("calibri", 12, "bold"), state="readonly" )
        row_no["value"]= ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T")
        row_no.grid(row=3, column=1)

        # == Column Number ==
        lbl_Column_no= Label(labelframeleft,text="Book Column_No",font=("Calibri", 12, "bold"), padx=2, pady=6)
        lbl_Column_no.grid(row=4, column=0,sticky=W)
        
        Column_No = ttk.Combobox(labelframeleft, textvariable=self.var_Column_No,width=33, font=("calibri", 12, "bold"),state="readonly")
        Column_No["value"]= (1,2,3,4,5,6,7,8,9,10)
        Column_No.grid(row=4, column=1)

        # == Language Combo Box ==
        lbl_Language= Label(labelframeleft,text="Language",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Language.grid(row=5, column=0,sticky=W)

        box_Language= ttk.Combobox(labelframeleft, textvariable=self.var_Language,font=("calibri",12), width=33, state="readonly")
        box_Language["value"]= ("Hindi", "English")
        box_Language.grid(row=5, column=1)

        # == Stu_Ref_No ==
        lbl_Books_writer= Label(labelframeleft,text=" Stu. Ref. No.",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Books_writer.grid(row=6, column=0,sticky=W)
        
        enty_writer = ttk.Entry(labelframeleft,textvariable=self.var_Stu_Ref_No,width=35, font=("calibri", 12))
        enty_writer.grid(row=6, column=1)

        # == Stu_Name ==
        lbl_Books_writer= Label(labelframeleft,text=" Stu. Name",font=("Calibri", 12, "bold"), padx=2, pady=8)
        lbl_Books_writer.grid(row=7, column=0,sticky=W)
        
        enty_writer = ttk.Entry(labelframeleft,textvariable=self.var_Stu_Name,width=35, font=("calibri", 12))
        enty_writer.grid(row=7, column=1)


        #============================ Button =================================
        btn_frame = Frame(labelframeleft,bd =2, relief=RIDGE)
        btn_frame.place(x=10, y=300, width=403, height=120)

        btn_Add = Button(btn_frame, text= "Add", command=self.add_data,font=("calibri", 13, "bold"), bg= "green", fg="Black", width=20, cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=5,pady=9)

        btn_Update = Button(btn_frame, text="Update", command=self.update,font=("calibri", 13, "bold"), bg= "gray", fg="Black", width=20, cursor="hand2")
        btn_Update.grid(row=0, column=1, padx=5,pady=9)

        btn_Delete = Button(btn_frame, text="Delete", command=self.delete,font=("calibri", 13, "bold"), bg= "red", fg="Black", width=20, cursor="hand2")
        btn_Delete.grid(row=1, column=0, padx=5,pady=9)

        btn_Reset = Button(btn_frame, text="Reset", command=self.reset,font=("calibri", 13, "bold"), bg= "gray", fg="Black", width=20, cursor="hand2")
        btn_Reset.grid(row=1, column=1, padx=5,pady=9)


        #==================Search Table Frame ===============================

        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text=" Search and View Details", font=("calibri", 15, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=515)

        lbl_searchBY= Label(table_frame,text="Search By",font=("Calibri", 12, "bold"), bg="yellow", fg="black")
        lbl_searchBY.grid(row=0, column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        DropDwon_search= ttk.Combobox(table_frame, textvariable=self.search_var,font=("calibri",12), width=20, state="readonly")
        DropDwon_search["value"]= ("Serial_No","Book_Name")
        DropDwon_search.grid(row=0, column=1, padx=2)

        self.text_search=StringVar()
        enty_search = ttk.Entry(table_frame, textvariable=self.text_search,width=24, font=("calibri", 12))
        enty_search.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, text="Search",command=self.search,font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9, cursor="hand2")
        btn_search.grid(row=0, column=3, padx=2)

        btn_showAll = Button(table_frame, text="Show All",command=self.fetch_data,font=("claibli", 12, "bold"), bg= "gray", fg="Black", width=9, cursor="hand2")
        btn_showAll.grid(row=0, column=4, padx=2)


        # ====================== Show Book Record Table =================================

        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x= ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Book_Records_Table= ttk.Treeview(details_table, columns=("serial no", "name","writer","row no", "column no",
                                            "Language","stu ref no", "stu name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Book_Records_Table.xview)
        scroll_y.config(command=self.Book_Records_Table.yview)

        self.Book_Records_Table.heading("serial no", text="Book Sr. No.")
        self.Book_Records_Table.heading("name", text="Book Name")
        self.Book_Records_Table.heading("writer", text="Writers Name")
        self.Book_Records_Table.heading("row no", text="Book Row No.")
        self.Book_Records_Table.heading("column no", text="Book Col. No.")
        self.Book_Records_Table.heading("Language", text="Book Language")
        self.Book_Records_Table.heading("stu ref no", text="Stu_Ref_No")
        self.Book_Records_Table.heading("stu name", text="Stu_Name")

        self.Book_Records_Table["show"]= "headings"

        self.Book_Records_Table.column("serial no", width= 80)
        self.Book_Records_Table.column("name", width= 80)
        self.Book_Records_Table.column("writer", width= 80)
        self.Book_Records_Table.column("row no", width= 80)
        self.Book_Records_Table.column("column no", width= 80)
        self.Book_Records_Table.column("Language", width= 80)
        self.Book_Records_Table.column("stu ref no", width= 80)
        self.Book_Records_Table.column("stu name", width= 80)        


        self.Book_Records_Table.pack(fill=BOTH, expand=1)
        self.Book_Records_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Serial_No.get()=="" or self.var_Book_Name.get()=="":
            messagebox.showerror("Error", "All Entry are required")
        else:
            try:
                conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Book_Records values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_Serial_No.get(),
                                                                                    self.var_Book_Name.get(),
                                                                                    self.var_Writers_Name.get(),
                                                                                    self.var_Row_No.get(),
                                                                                    self.var_Column_No.get(),
                                                                                    self.var_Language.get(),
                                                                                    self.var_Stu_Ref_No.get(),
                                                                                    self.var_Stu_Name.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Book Record has been added", parent= self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Book_Records")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Book_Records_Table.delete(*self.Book_Records_Table.get_children())
            for i in rows:
                self.Book_Records_Table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row= self.Book_Records_Table.focus()
        content= self.Book_Records_Table.item(cursor_row)
        row= content["values"]

        self.var_Serial_No.set(row[0]),
        self.var_Book_Name.set(row[1]),
        self.var_Writers_Name.set(row[2]),
        self.var_Row_No.set(row[3]),
        self.var_Column_No.set(row[4]),
        self.var_Language.set(row[5]),
        self.var_Stu_Ref_No.set(row[6]),
        self.var_Stu_Name.set(row[7])



    def update(self):
        if self.var_Serial_No.get()=="":
            messagebox.showerror("Enter", "Please Enter Book Serial Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()                                                                                                                          
            my_cursor.execute("update Book_Records set Book_Name=%s,Writers_Name=%s, Book_Row_No=%s,Book_Column_No=%s, Language=%s, Stu_Ref_No=%s, Stu_Name=%s where Serial_No=%s",(
                                                                                                                                                         self.var_Book_Name.get(),
                                                                                                                                                         self.var_Writers_Name.get(),
                                                                                                                                                         self.var_Row_No.get(),
                                                                                                                                                         self.var_Column_No.get(),
                                                                                                                                                         self.var_Language.get(),                                                                                                    
                                                                                                                                                         self.var_Stu_Ref_No.get(),
                                                                                                                                                         self.var_Stu_Name.get(),
                                                                                                                                                         self.var_Serial_No.get()

                                                                                                                                                     ))   
            conn.commit()
            self.fetch_data()
            conn.close()                                                             
            messagebox.showinfo("Update","Book Records has been updated successfully",parent=self.root)


    def delete(self):
        smsdelete = messagebox.askyesno("Library_Management_System", "Do you want to delete this Book Record",parent=self.root)
        if smsdelete>0:
            conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
            my_cursor=conn.cursor()
            query = "delete from Book_Records where Serial_No=%s"
            value =(self.var_Serial_No.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Serial_No.set(""),
        self.var_Book_Name.set(""),
        self.var_Writers_Name.set(""),
        self.var_Row_No.set(""),
        self.var_Column_No.set(""),
        self.var_Language.set("")
        self.var_Stu_Ref_No.set("")
        self.var_Stu_Name.set("")

        x= random.randint(1,499)
        self.var_Serial_No.set(str(x))


    #== Search By===
    def search(self):
        conn= mysql.connector.connect(host= "localhost",username="root",password="Man9690@", database="Library_Management_System")
        my_cursor=conn.cursor()

        query = "SELECT * FROM Book_Records WHERE " + self.search_var.get() + " LIKE %s"
        search_term = "%" + self.text_search.get() + "%"

        my_cursor.execute(query, (search_term,))
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.Book_Records_Table.delete(*self.Book_Records_Table.get_children())
            for i in rows:
                self.Book_Records_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Books_Record(root)
    root.mainloop()