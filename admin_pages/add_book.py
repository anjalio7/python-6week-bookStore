# from curses import window
# from cProfile import label
from logging import root
from tkinter import *
# from turtle import bgcolor, width
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
from tkinter.ttk import Combobox
import database
import admin_menu

 

class AddBook:
    def __init__(self, window):
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

  
        
        self.txt = "ADD BOOK  "
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=800, height=30)

        
        


        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_label = Label(self.lgn_frame, text="BOOK NAME", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=320, y=100)
        
        self.sign_in_label2 = Label(self.lgn_frame, text="BOOK CATEGORY", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label2.place(x=352, y=180)
        
        self.sign_in_label3 = Label(self.lgn_frame, text="BOOK AUTHOR", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label3.place(x=340, y=260)
        
        self.sign_in_label4 = Label(self.lgn_frame, text="BOOK  PRICE ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label4.place(x=330, y=340)
        
        self.sign_in_label5 = Label(self.lgn_frame, text="RACK NO. /     \n COLUMN          ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 2, width=30)
        self.sign_in_label5.place(x=330, y=415)
        
        self.sign_in_label6 = Label(self.lgn_frame, text="STOCK             ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label6.place(x=335, y=510)
        


#################################### ########## ENTRY  ###################################################  ######################################################################################################################################


        self.username_entry = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry.place(x=900, y=166, width=220)
        
        # self.username_entry2 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
        #                            borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        # self.username_entry2.place(x=900, y=247, width=220)
        
        self.username_entry3 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry3.place(x=900, y=325, width=220)
        
        self.username_entry4 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry4.place(x=900, y=409, width=220)
        
        # self.username_entry5 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
        #                            borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        # self.username_entry5.place(x=900, y=493, width=220)
        
        self.username_entry6 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry6.place(x=900, y=577, width=220)
        
        
        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        
        
        self.side_image = Image.open('images\\addbook3.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=80)
                
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label7 = Button(self.lgn_frame, text="ADD BOOK", bg="BLUE", fg="white", command= self.loginUser , 
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=25)
        self.sign_in_label7.place(x=50, y=500)

        
        # ========================================================================
        # ================================DROP DOWN MENU  ========================
        # ========================================================================


        self.dropValue = StringVar()
        print("manage",database.allCategories)
        self.options= database.allCategories()
        print(self.options)
        self.drop_Down = Combobox(self.window, textvariable=self.dropValue, values= self.options)
        self.drop_Down.place(x=905,y=250 , height=34, width= 212)  
        


        self.dropValue2 = StringVar()
        print("manage",database.singlerack)
        self.options= database.singlerack()
        print(self.options)
        self.drop_Down = Combobox(self.window, textvariable=self.dropValue2, values= self.options)
        self.drop_Down.place(x=905,y=500 , height=34, width= 212)  

                # /////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////GO BACK PHOTO ////////////////////////////
        # //////////////////////////////////////////////////////////////////////////
        self.lgn_button = Image.open('images\\back1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Button(self.lgn_frame, image=photo, bg='#040405',command=self.adminpage)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=0, y=0)

    def adminpage(self):
        obj= admin_menu.menupage(self.window)
        self.window.destroy()

        
        
    
    
    def loginUser(self):
            
        if self.username_entry.get()  == '':
            messagebox.showerror('Alert', 'Enter Name first.')
            
        elif self.dropValue.get() == '':
            messagebox.showerror('Alert', 'Enter Book category first.')
        
        elif self.username_entry3.get() == '' :
            messagebox.showerror('Alert', 'Enter Book Author  first.')
        
        elif self.username_entry4.get() == '' :
            messagebox.showerror('Alert', 'Enter Book price first')
               
        
        # elif self.username_entry5.get() == '' :
        #     messagebox.showerror('Alert', 'Enter Rack Number first')
               
        
        elif self.username_entry6.get() == '' :
            messagebox.showerror('Alert', 'Enter No. of Books first')
               
        
        elif self.username_entry4.get() == '0' :
            messagebox.showerror('Alert', 'Book price cannot be 0.')

            
        elif not(self.username_entry4.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter numbers in book price.')
            
        # elif (self.username_entry5.get().isdigit()):
            # messagebox.showerror('Alert', 'You can only enter numbers in  rack no. ')
            
        elif not(self.username_entry6.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter numbers in Stock.')
            
            
        else:
            # messagebox.showinfo('Success', 'Added Successfully.')
            self.data = (
                self.username_entry.get(),
                self.dropValue.get().split()[0],
                self.username_entry3.get(),
                self.username_entry4.get(),
                self.dropValue2.get().split()[0],
                self.username_entry6.get(),
                )
            
            print(self.data)

            res = database.AddBooks(self.data)
            if res:        
                messagebox.showinfo('Success', 'Book added successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
            
                

def page():
    window = Toplevel()
    AddBook(window)
    # LoginPage.comboWidget(window)
    window.mainloop()


if __name__ == '__main__':
    page()