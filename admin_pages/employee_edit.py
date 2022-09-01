from logging import root
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
from tkinter.ttk import Combobox
import database
import admin_menu
import book_tables

class ADDEmployee:
    def __init__(self, window,id):
        self.id=id
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('BOOK STORE MANAGEMENT SYSTEM ')

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

  
        
        self.txt = "EDIT EMPLOYEE  "
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=800, height=30)

        
        


        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_label = Label(self.lgn_frame, text="EMOLOYEE NAME", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=320, y=100)
        
        self.sign_in_label2 = Label(self.lgn_frame, text="EMAIL", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label2.place(x=250, y=180)
        
        self.sign_in_label3 = Label(self.lgn_frame, text="PHONE NO ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label3.place(x=279, y=260)
        
        self.sign_in_label4 = Label(self.lgn_frame, text="USERNAME  ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label4.place(x=285, y=340)
        
        self.sign_in_label5 = Label(self.lgn_frame, text="PASSWORD", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 2, width=30)
        self.sign_in_label5.place(x=280, y=415)


        


#################################### ########## ENTRY  ###################################################  ######################################################################################################################################


        self.username_entry = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry.place(x=900, y=166, width=220)
        
        self.username_entry2 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry2.place(x=900, y=247, width=220)
        
        self.username_entry3 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry3.place(x=900, y=325, width=220)
        
        self.username_entry4 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry4.place(x=900, y=409, width=220)
        
        self.username_entry5 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry5.place(x=900, y=493, width=220)
        

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        
        
        self.side_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=160)
                
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label6 = Button(self.lgn_frame, text="EDIT EMPLOYEE", bg="BLUE", fg="white", command= self.loginUser , 
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=25)
        self.sign_in_label6.place(x=300, y=500)


        # /////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////GO BACK PHOTO ////////////////////////////
        # //////////////////////////////////////////////////////////////////////////
        
        
        self.goback_button = Image.open('images\\back1.png')
        photo = ImageTk.PhotoImage(self.goback_button)
        self.goback_button_label = Button(self.lgn_frame, image=photo, bg='#040405',command=self.adminpage)
        self.goback_button_label.image = photo
        self.goback_button_label.place(x=0 ,y=0)
 
 
        res = database.singleEmployee(self.id)
        print(res)
        if res:
            self.username_entry.insert(0, res[1])
            self.username_entry2.insert(0, res[2])
            self.username_entry3.insert(0, res[3])
            self.username_entry4.insert(0, res[4])
            self.username_entry5.insert(0, res[5])
        else:
            messagebox.showerror('Alert', 'something went wrong')       
        
        

    def adminpage(self):
        obj= admin_menu.menupage(self.window)
        
        
        
    def loginUser(self):
            
        if self.username_entry.get()  == '':
            messagebox.showerror('Alert', 'Enter Name first.')
            
        elif self.username_entry2.get() == '':
            messagebox.showerror('Alert', 'Enter Email First .')
        
        elif self.username_entry3.get() == '' :
            messagebox.showerror('Alert', 'Enter Phone Number  first.')
        
        elif self.username_entry4.get() == '' :
            messagebox.showerror('Alert', 'Enter Username first')
               
        
        elif self.username_entry5.get() == '' :
            messagebox.showerror('Alert', 'Enter Password  first')
               
        elif (self.username_entry.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter Alphabets In Name .')

            
        elif not(self.username_entry3.get().isdigit()):
            messagebox.showerror('Alert', 'Youcan only enter Numbers In Phone No. ')
            
            
            
            
        else:
            # messagebox.showinfo('Success', 'Added Successfully.')
            self.data = (
                self.username_entry.get(),
                self.username_entry2.get(),
                self.username_entry3.get(),
                self.username_entry4.get(),
                self.username_entry5.get(),
                self.id[0]
                )

            res = database.editEmployee(self.data)
            if res:        
                messagebox.showinfo('Success', 'Employee added successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
                
                
                
def page(id):
    window = Toplevel()
    ADDEmployee(window,id)
    window.mainloop()


if __name__ == '__main__':
    page()