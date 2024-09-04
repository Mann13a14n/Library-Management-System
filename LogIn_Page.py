from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from Library_Management_System import LibraryManagementSystem
from Register import register


def main():
    win= Tk()
    app = Login_Win(win)
    win. mainloop()



class Login_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        #============= Image ===============
        
        self.bg= ImageTk.PhotoImage(file=r"C:\Users\manth\Downloads\Library Project\5.jpg")

        lbl_bg= Label(self.root, image= self.bg)
        lbl_bg.place(x=0 , y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="light blue")
        frame.place(x=610, y= 170, width=340, height=450)

        img1 = Image.open(r"C:\Users\manth\Downloads\Library Project\10.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1= Label(image=self.photoimg1, bg="black", borderwidth=0)
        lbl_img1.place(x= 730, y=178, width=100, height=100)

        welcome= Label(frame, text="Let's Go", font=("calibri", 16, "bold"),fg= "black", bg="light blue")
        welcome.place(x=130, y=105)

        # == label ==
        username = Label(frame, text= "Username / Email Id", font=("calibri", 15, "bold"), fg="black", bg="light blue")
        username.place(x= 80, y= 155)

        self.usertxt = Entry(frame, font=("calibri", 15, "bold"))
        self.usertxt.place(x=40 , y=190, width=270)

        password = Label(frame, text= "Password", font=("calibri", 15, "bold"), fg="black", bg="light blue")
        password.place(x= 120, y= 230)

        self.passtxt = Entry(frame, font=("calibri", 15, "bold"), show="*")
        self.passtxt.place(x=40 , y=265, width=270)


        # === Button =======
        btn_Login = Button(frame, text= "Log In", command=self.login, font=("calibri", 15, "bold"), bg= "black", fg="White", width=20, cursor="hand2")
        btn_Login.place(x=110 , y=310, width=120, height=35)

        btn_Register = Button(frame, text="New User Register", command=self.Register_form,font=("calibri", 13, "bold"),borderwidth=0, fg="Black", bg="light blue", activebackground="light blue", cursor="hand2")
        btn_Register.place(x=25 , y=360, width=160)

        btn_Forget = Button(frame, text="Forget Password", command=self.forget_pass_win,font=("calibri", 13, "bold"), borderwidth=0, fg="Black", bg="light blue", activebackground="light blue", cursor="hand2")
        btn_Forget.place(x=18 , y=390, width=160)

    def register_win(self):
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)


    def login(self):
        if self.usertxt.get()== "" or self.passtxt.get()== "":
            messagebox.showerror("Error", "All Field Required")
        elif self.usertxt.get()=="Manthan" and self.passtxt.get()=="Man@9690":
            messagebox.showinfo("Success", "Welcome Mr. Manthan")
        else:
            conn = mysql.connector.connect(host ="localhost", username ="root", password="Man9690@", database="Library_Management_System")
            my_cur = conn.cursor()
            my_cur.execute("select * from Register where Email=%s and Password=%s",(
                                                                                    self.usertxt.get(),
                                                                                    self.passtxt.get()

                                                                                    ))
            row = my_cur.fetchone()
            if row== None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Do you want to Login")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = LibraryManagementSystem(self.new_window)
                    self.usertxt.delete(0, END)
                    self.passtxt.delete(0, END)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


     # ============================== Rest Password ============================================ 

    def reset_pass(self):
        if self.box_sq.get()=="":
            messagebox.showerror("Error", "Please Select Security Question",parent=self.root2)
        elif self.S_answer.get()=="":
            messagebox.showerror("Error", "Please Enter Your Security Answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error", "Please Enter Your New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host ="localhost", username ="root", password="Man9690@", database="Library_Management_System")
            my_cur = conn.cursor()
            query = ("Select * from Register where Email=%s and S_Que=%s and S_Ans=%s")
            value = (self.usertxt.get(), self.box_sq.get(), self.S_answer.get())
            my_cur.execute(query, value)
            row = my_cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter Correct Answer",parent=self.root2)
            else:
                query = ("update Register set Password=%s where Email=%s")
                value= self.new_password.get(), self.usertxt.get()
                my_cur.execute(query, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", " Your Password has been Updated, Please LogIn with New Password",parent=self.root2)
                self.root2.destroy()


    def forget_pass_win(self):
        if self.usertxt.get()=="":
            messagebox.showerror("Error", " Please Enter the Email Id to reset your Password")
        else:
            conn = mysql.connector.connect(host ="localhost", username ="root", password="Man9690@", database="Library_Management_System")
            my_cur = conn.cursor()
            query = ("select * from Register where Email=%s")
            value = (self.usertxt.get(),)
            my_cur.execute(query, value)
            row = my_cur.fetchone()
            #print(row)

            if row == None:
                messagebox.showerror("Error", "Please Enter a valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                Lb = Label(self.root2, text="Forget Password", font=("calibri", 18, "bold"), fg="black", bg="dark gray")
                Lb.place(x=0, y=10, relwidth=1)

                # ======== Security Question ========
                lbl_sq= Label(self.root2,text="Select Security Question",font=("Calibri", 15, "bold"))
                lbl_sq.place(x=40 , y=80)
                
                self.box_sq= ttk.Combobox(self.root2,font=("calibri",12, "bold"), width=30, state="readonly")
                self.box_sq["value"]= ("Select","Father's Name", "First School Name", "Your Dream Job", "Your Pet Name", "Birth Place", "Favourite Actor")
                self.box_sq.current(0)
                self.box_sq.place(x=40 , y= 120)

                #=== Security Answer ====
                lbl_answer= Label(self.root2,text="Security Answer",font=("Calibri", 15, "bold"))
                lbl_answer.place(x=40 , y=150)
                
                self.S_answer = ttk.Entry(self.root2,width=32, font=("calibri", 12, "bold"))
                self.S_answer.place(x=40 , y=190)

                #=== Password ====
                lbl_password1= Label(self.root2,text="New Password",font=("Calibri", 15, "bold"))
                lbl_password1.place(x=40 , y=220)
                
                self.new_password = ttk.Entry(self.root2,width=32, font=("calibri", 12, "bold"))
                self.new_password.place(x=40 , y=260)

                # === Submit =========
                btn_Submit = Button(self.root2, text= "Reset", command=self.reset_pass, font=("calibri", 15, "bold"), bg= "black", fg="White", width=20, cursor="hand2")
                btn_Submit.place(x=100 , y=330, width=120, height=35)






    def Register_form(self):
        self.new_window= Toplevel(self.root)
        self.app= register(self.new_window)






if __name__ == "__main__":
    main()

        