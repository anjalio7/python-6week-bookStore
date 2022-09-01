# from curses import window
# from cProfile import label
from logging import root
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
import admin_menu
import database

 

class Category:
    def __init__(self, window,id):
        self.id=id
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('UPDATE CATEGORY')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        
        
        # ====== background Frame =========================
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
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_label = Label(self.lgn_frame, text="  CATEGORY NAME", bg="#040405", fg="white",
                                    font=("yu gothic ui", 27, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=335, y=170)
        
        
        
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label5 = Button(self.lgn_frame, text="UPDATE CATEGORY", bg="BLUE", fg="white", command= self.loginUser , 
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label5.place(x=460, y=470)


                # /////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////GO BACK PHOTO ////////////////////////////
        # //////////////////////////////////////////////////////////////////////////
        self.lgn_button = Image.open('images\\back1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Button(self.lgn_frame, image=photo, bg='#040405',command=self.adminpage)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=0, y=0)

#################################### ########## ENTRY  ###################################################  ######################################################################################################################################


        self.username_entry = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry.place(x=750, y=346, width=250)
        

        
        
        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        
        
        self.side_image = Image.open('images\\addbook3.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=80)
  
  
        res = database.singleCategory(self.id)
        print(res)
        if res:
            self.username_entry.insert(0, res[1])
        else:
            messagebox.showerror('Alert', 'something went wrong')
        
        
      
        
        
    def loginUser(self):
            
        if self.username_entry.get()  == '':
            messagebox.showerror('Alert', 'Enter Name first.')

            
        else:
            # messagebox.showinfo('Success', 'Added Successfully.')
            self.data = (
                self.username_entry.get(),
                self.id[0]
                )
            
            print(self.data)

            res = database.editCat(self.data)
            if res:        
                messagebox.showinfo('Success', 'Book added successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong.')


    def adminpage(self):
        obj= admin_menu.menupage(self.window)
        # self.window.destroy()
        

def page(id):
    window = Toplevel()
    Category(window,id)
    window.mainloop()


if __name__ == '__main__':
    page()