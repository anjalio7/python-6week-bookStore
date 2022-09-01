from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
import admin_menu
import pymysql
import database
import admin_login

import employeeLogin


class mainPage:
    def __init__(self, window):
        self.window = window
        window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "BOOK STORE MANAGEMENT SYSTEM "
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=800, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)
        
                # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=600, y=130)

        
        
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label6 = Button(self.lgn_frame, text="ADMIN LOGIN", bg="RED", fg="white", command=self.openadmin,
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=25)
        self.sign_in_label6.place(x=500, y=300)
        
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label6 = Button(self.lgn_frame, text="EMPLOYEE LOGIN", bg="BLUE", fg="white", command=self.openemployee,
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=25)
        self.sign_in_label6.place(x=500, y=400)

    def openadmin(self):
        obj = admin_login.LoginPage(self.window)
    
    def openemployee(self):
        obj2 = employeeLogin.EmployeeLogin(self.window)
        
 
  
 


def page():
    window = Tk()
    mainPage(window)
    window.mainloop()
    
if __name__ == '__main__': 
    page()