# from curses import window
# from cProfile import label
from logging import root
from platform import win32_edition
from tkinter import *
# from turtle import bgcolor, width
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
from tkinter.ttk import Combobox
import database
import admin_menu

class Racks:
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

  
        
        self.txt = "EDIT RACKS"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=800, height=30)

        
        


        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_label = Label(self.lgn_frame, text="RACK NAME", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=320, y=150)
        
        self.sign_in_label2 = Label(self.lgn_frame, text="NO. OF ROWS ", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label2.place(x=330, y=230)
        
        self.sign_in_label3 = Label(self.lgn_frame, text="TOTAL CAPACITY", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label3.place(x=350, y=310)
        
        self.sign_in_label4 = Label(self.lgn_frame, text="CAPACITY / ROW", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold") , height= 2, width=30)
        self.sign_in_label4.place(x=347, y=380)
        



#################################### ########## ENTRY  ###################################################  ######################################################################################################################################


        self.username_entry = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry.place(x=900, y=216, width=220)
        
        self.username_entry2 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry2.place(x=900, y=297, width=220)
        
        self.username_entry3 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry3.place(x=900, y=375, width=220)
        
        self.username_entry4 = Entry(self.window, highlightthickness=0,  relief= 'solid', bg="#C4A484", fg="black",
                                   borderwidth= 5 ,   font=("yu gothic ui ", 18, "bold") )
        self.username_entry4.place(x=900, y=459, width=220)
        

        
        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        
        
        self.side_image = Image.open('images\\addbook3.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=80)
                
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     BUTTON      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2      
        
        self.sign_in_label5 = Button(self.lgn_frame, text="ADD RACK", bg="BLUE", fg="white", command= self.loginUser , 
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=25)
        self.sign_in_label5.place(x=510, y=500)

                # /////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////GO BACK PHOTO ////////////////////////////
        # //////////////////////////////////////////////////////////////////////////
        self.goback_button = Image.open('images\\back1.png')
        photo = ImageTk.PhotoImage(self.goback_button)
        self.goback_button_label = Button(self.lgn_frame, image=photo, bg='#040405',command=self.adminpage)
        self.goback_button_label.image = photo
        self.goback_button_label.place(x=0 ,y=0)
        
        res = database.singleRack(self.id)
        print(res)
        if res:
            self.username_entry.insert(0, res[1])
            self.username_entry2.insert(0, res[2])
            self.username_entry3.insert(0, res[3])
            self.username_entry4.insert(0, res[4])
        else:
            messagebox.showerror('Alert', 'something went wrong')    

    def adminpage(self):
        obj= admin_menu.menupage(self.window)
        self.window.destroy()
        



        
    def loginUser(self):
            
        if self.username_entry.get()  == '':
            messagebox.showerror('Alert', 'Enter Rack Name first.')

        elif self.username_entry3.get() == '' :
            messagebox.showerror('Alert', 'Enter rack capacity first.')
        
        elif self.username_entry4.get() == '' :
            messagebox.showerror('Alert', 'Enter rack capacity per row first')
               
    
        elif self.username_entry4.get() == '0' :
            messagebox.showerror('Alert', 'Book price cannot be 0.')

            
        elif not(self.username_entry2.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter numbers in rows.')
            
        elif not(self.username_entry3.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter numbers in rack capacity.')
            
        elif not(self.username_entry4.get().isdigit()):
            messagebox.showerror('Alert', 'You can only enter numbers in rack capacity per row.')

        else:
            # messagebox.showinfo('Success', 'Added Successfully.')
            self.data = (
                self.username_entry.get(),
                self.username_entry2.get(),
                self.username_entry3.get(),
                self.username_entry4.get(),
                self.id[0]
                )

            res = database.editrack( self.data)
            if res:        
                messagebox.showinfo('Success', 'Rack added successfully.')
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
                

        

def page(id):
    window = Toplevel()
    Racks(window,id)
    # LoginPage.comboWidget(window)
    window.mainloop()


if __name__ == '__main__':
    page()