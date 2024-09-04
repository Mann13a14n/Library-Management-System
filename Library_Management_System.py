from tkinter import*
from PIL import Image, ImageTk
from Student import Stu_Win
from Seat import Seat_Registration
from Books import Books_Record
from Seat_Details import Details
from Report import Report

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # ==================insert Image ==================================
        
        img1 = Image.open(r"C:\Users\manth\Downloads\Library Project\1.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)
        
        # ==================Logo Image ==================================
        
        img2 = Image.open(r"C:\Users\manth\Downloads\Library Project\2.jpg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=190, height=140)
        
        # ==================  Title  ========================
        
        lbl_title = Label(self.root,text="WELCOME  TO  MS  LIBRARY", font=("Calibri", 35, "bold"),bg="gray", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y= 140, width= 1550, height=50)
        
        
        # ================== Frame =======================
        
        main_frame = Frame(self.root,bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)
        
        
        # ================== Inquiry Section ======================
        
        lbl_inquiry = Label(main_frame,text="INQUIRY SECTION", font=("Calibri", 16, "bold"),bg="black", fg="white", bd=4,relief=RIDGE)
        lbl_inquiry.place(x=0, y= 0, width= 229)
        
         # ==================Button Frame =======================
        
        btn_frame = Frame(main_frame,bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=32, width=228, height=248)
        
        # ================== Button =======================
        
        stu_btn=Button(btn_frame, text="STUDENT",command=self.stu_details, width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        stu_btn.grid(row=0, column= 0, pady= 2)
        
        seat_btn=Button(btn_frame, text="SEAT NO", command=self.Seat_details, width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        seat_btn.grid(row=1, column= 0, pady= 2)
        
        
        book_btn=Button(btn_frame, text="BOOK",command=self.Books_Details , width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        book_btn.grid(row=2, column= 0, pady= 2)
        
        
        details_btn=Button(btn_frame, text="DETAILS", command=self.Seat_Detail, width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        details_btn.grid(row=3, column= 0, pady= 2)
        
        report_btn=Button(btn_frame, text="COMPLAINT", command=self.Reports, width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        report_btn.grid(row=4, column= 0, pady= 2)
        
        logout_btn=Button(btn_frame, text="LOGOUT", command=self.logout, width=22,font=("Calibri", 14, "bold"),bg="gray", fg="black", bd=0,cursor="hand2")
        logout_btn.grid(row=5, column= 0, pady= 2)
        
        
        # ====================== Right Side Image ==============================
        
        img3 = Image.open(r"C:\Users\manth\Downloads\Library Project\3.jpg")
        img3 = img3.resize((1320, 610), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1320, height=610)
        
        # ======================= Left Side Image =============================
        
        img4 = Image.open(r"C:\Users\manth\Downloads\Library Project\Mann.jpg")
        img4 = img4.resize((270, 370), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=278, width=228, height=330)
        
    def stu_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Stu_Win(self.new_window)


    def Seat_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Seat_Registration(self.new_window)


    def Books_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Books_Record(self.new_window)


    def Seat_Detail(self):
        self.new_window= Toplevel(self.root)
        self.app= Details(self.new_window)

    def Reports(self):
        self.new_window= Toplevel(self.root)
        self.app= Report(self.new_window)


    def logout(self):
        self.root.destroy()
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()


