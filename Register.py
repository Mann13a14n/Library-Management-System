from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #============= Varible ============

        self.var_1stName = StringVar()
        self.var_2ndName = StringVar()
        self.var_contact = StringVar()
        self.var_emailId = StringVar()
        self.var_S_Que = StringVar()
        self.var_S_Ans = StringVar()
        self.var_password = StringVar()
        self.var_conf_pass = StringVar()
        self.var_checkbtn = IntVar()
        


        #==== Lable Background Image ================
        img1 = Image.open(r"C:\Users\manth\Downloads\Library Project\6.jpg")
        img1 = img1.resize((445, 800), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl= Label(self.root, image=self.photoimg1)
        lbl.place(x=0 , y=0, width=450, height=800)

        #========= Frame ==============
        lbl_register = LabelFrame(self.root, bd=2, relief=RIDGE, text="Register Here", font=("calibri", 20, "bold"), padx=2)
        lbl_register.place(x=450, y=50, width=860, height=515)

        # ======== Lable and Entry =================

        # == First Name ==
        lbl_first_name= Label(lbl_register,text="First Name", font=("Calibri", 15, "bold"))
        lbl_first_name.place(x=50 , y=10)
        
        enty_first = ttk.Entry(lbl_register, textvariable=self.var_1stName,width=35, font=("calibri", 12, "bold"))
        enty_first.place(x=50 , y=39)

        # == Last Name ==
        lbl_Last_name= Label(lbl_register,text="Last Name",font=("Calibri", 15, "bold"))
        lbl_Last_name.place(x=400 , y=10)
        
        enty_Last_name = ttk.Entry(lbl_register, textvariable=self.var_2ndName,width=35, font=("calibri", 12, "bold"))
        enty_Last_name.place(x=400 , y=39)

        #=== Contact Number ====
        lbl_contact_no= Label(lbl_register,text="Contact Number",font=("Calibri", 15, "bold"))
        lbl_contact_no.place(x=50 , y=70)
        
        enty_contact_no = ttk.Entry(lbl_register, textvariable=self.var_contact,width=35, font=("calibri", 12, "bold"))
        enty_contact_no.place(x=50 , y=97)

        #=== Eamil ID ====
        lbl_email_id= Label(lbl_register,text="Email Id / Username ",font=("Calibri", 15, "bold"))
        lbl_email_id.place(x=400 , y=70)
        
        enty_email_id = ttk.Entry(lbl_register, textvariable=self.var_emailId,width=35, font=("calibri", 12, "bold"))
        enty_email_id.place(x=400 , y=97)


        # ======== Security Question ========
        lbl_sq= Label(lbl_register,text="Select Security Question",font=("Calibri", 15, "bold"))
        lbl_sq.place(x=50 , y=130)
        
        box_sq= ttk.Combobox(lbl_register, textvariable=self.var_S_Que,font=("calibri",12, "bold"), width=33, state="readonly")
        box_sq["value"]= ("Select","Father's Name", "First School Name", "Your Dream Job", "Your Pet Name", "Birth Place", "Favourite Actor")
        box_sq.current(0)
        box_sq.place(x=50 , y= 161)

        #=== Security Answer ====
        lbl_answer= Label(lbl_register,text="Security Answer",font=("Calibri", 15, "bold"))
        lbl_answer.place(x=400 , y=130)
        
        enty_answer = ttk.Entry(lbl_register, textvariable=self.var_S_Ans,width=35, font=("calibri", 12, "bold"))
        enty_answer.place(x=400 , y=161)

        #=== Password ====
        lbl_password1= Label(lbl_register,text="Password",font=("Calibri", 15, "bold"))
        lbl_password1.place(x=50 , y=197)
        
        enty_password1 = ttk.Entry(lbl_register, textvariable=self.var_password,width=35, font=("calibri", 12, "bold"), show="*")
        enty_password1.place(x=50 , y=225)

        #=== Confirm Password ====
        lbl_confirm_pass= Label(lbl_register,text="Confirm Password",font=("Calibri", 15, "bold"))
        lbl_confirm_pass.place(x=400 , y=197)
        
        enty_confirm_pass = ttk.Entry(lbl_register, textvariable=self.var_conf_pass,width=35, font=("calibri", 12, "bold"))
        enty_confirm_pass.place(x=400 , y=225)

        #======== Check Button ============
        chk_btn = Checkbutton(lbl_register, variable=self.var_checkbtn, text="I agree the terms and conditions", font=("Calibri", 15, "bold"), bg="dark gray", onvalue=1, offvalue=0)
        chk_btn.place(x=50, y=270)


        # === Button =======
        btn_Register_Now = Button(lbl_register, text= "Register Now", command=self.register_data, font=("calibri", 15, "bold"), bg= "black", fg="White", width=40, cursor="hand2")
        btn_Register_Now.place(x=100 , y=360, width=150, height=35)

        # === LogIn Now =========
        btn_Login_now = Button(lbl_register, command=self.return_login, text= "LogIn Now", font=("calibri", 15, "bold"), bg= "black", fg="White", width=20, cursor="hand2")
        btn_Login_now.place(x=400 , y=360, width=120, height=35)

        # ====================== Function declaration ===================

    def register_data(self):
        if self.var_1stName.get()== "" or self.var_emailId.get()== "" or self.var_S_Que.get()== "Select":
              messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get()!= self.var_conf_pass.get():
              messagebox.showerror("Error", "Password and Confirm Password is not same")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error", "Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host ="localhost", username ="root", password="Man9690@", database="Library_Management_System")
            my_cur = conn.cursor()
            query = ("Select * from Register where Email=%s")
            value = (self.var_emailId.get(),)
            my_cur.execute(query, value)
            row = my_cur.fetchone()
            if row!= None:
                messagebox.showerror("Error", " User already registered, Please try another Email")
            else:
                my_cur.execute("insert into Register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_1stName.get(),
                                                                                    self.var_2ndName.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_emailId.get(),
                                                                                    self.var_S_Que.get(),
                                                                                    self.var_S_Ans.get(),
                                                                                    self.var_password.get()

                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")
            

    def return_login(self):
        self.root.destroy()
    




if __name__ == "__main__":
    root = Tk()
    app = register(root)
    root.mainloop()