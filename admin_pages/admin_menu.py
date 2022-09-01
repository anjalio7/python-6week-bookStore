
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
import add_book, database
import book_tables
import add_employee
import employee_tables
import racks
import racks_tables
import category
import edit_books_tables
import bill1
import categories_tables
# import order_tables
import viewOrders
class menupage:
    
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('ADMIN MENU')
        
        
        
        # ========================================================================
        # ================================    MENU BAR   =======================
        # ========================================================================
        
        
        self.menubar = Menu(self.window)  
        self.file = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file.add_command(label="Add Books" ,command=self.addbook)  
        self.file.add_command(label="Add Category" ,command=self.addcategory)  
        self.file.add_command(label="Delete Books",command=self.viewbook )  
        self.file.add_command(label="Views Books",command=self.viewbook  )
        self.file.add_command(label="Edit Books",command=self.viewbook  )
        # self.file.add_command(label="View racks",command=self.viewracks)  
        # self.file.add_command(label="View Bills")  
  
        self.file.add_separator()  
  
        self.file.add_command(label="Exit", command=self.window.quit)  
  
        self.menubar.add_cascade(label="Books", menu=self.file)  
        self.edit = Menu(self.menubar, tearoff=0)  
        self.edit.add_command(label="Undo")  

        self.file2 = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file2.add_command(label="Add Employee" ,command=self.addemployee)  
        self.file2.add_command(label="View Employees",command=self.viewemployee )  
        self.file2.add_command(label="Delete Employees",command=self.viewemployee  )
        self.file2.add_command(label="Edit Employees",command=self.viewemployee)  
        # self.file2.add_command(label="View Bills")  
        self.menubar.add_cascade(label="Employee", menu=self.file2)  
        

        self.file3 = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file3.add_command(label="Add Racks" ,command=self.racks)  
        self.file3.add_command(label="View Racks",command=self.viewracks)  
        self.file3.add_command(label="Edit Racks",command=self.viewracks)
        self.file3.add_command(label="Delete Racks",command=self.viewracks)  
        # self.file3.add_command(label="View Bils")  
        self.menubar.add_cascade(label="Racks", menu=self.file3)  
        

        self.file4 = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file4.add_command(label="View Bills" ,command=self.openBills)  
        self.file4.add_command(label="Generate Bills",command=self.bills )  
        # self.file4.add_command(label="Vews Books",command=self.viewbook  )
        # self.file4.add_command(label="Vi racks",command=self.viewracks)  
        # self.file4.add_command(label="View Bills")  
        self.menubar.add_cascade(label="Bills", menu=self.file4)  

        self.file5 = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file5.add_command(label="View Categories" ,command=self.viewCategories)  
        self.file5.add_command(label="Add Categories",command=self.addcategory)  
        # self.file4.add_command(label="Vews Books",command=self.viewbook  )
        # self.file4.add_command(label="Vi racks",command=self.viewracks)  
        # self.file4.add_command(label="View Bills")  
        self.menubar.add_cascade(label="Categories", menu=self.file5)  

        self.menubar.add_cascade(label='Logout', command=self.window.destroy)
        

        # self.file6 = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        # self.file6.add_command(label="View orders" ,command=self.vieworders)  
        # self.file6.add_command(label="Add Orders",command=self.addorder )  
        # # self.file4.add_command(label="Vews Books",command=self.viewbook  )
        # # self.file4.add_command(label="Vi racks",command=self.viewracks)  
        # # self.file4.add_command(label="View Bills")  
        # self.menubar.add_cascade(label="Orders", menu=self.file6)  
        
        self.window.config(menu=self.menubar)  
        

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

        self.sign_in_label = Label(self.lgn_frame, text=f'Employees : {len(database.totalEmp())}', bg="blue", fg="white", font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=390)
        
        #  for black backgorund colour=  bg="#040405"
        
        self.sign_in_label = Label(self.lgn_frame, text=f'Books : {len(database.totalBooks())}', bg="blue", fg="white", font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=230)
        
        self.sign_in_label = Label(self.lgn_frame, text=f'Racks : {len(database.totalRacks())}', bg="blue", fg="white", font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=310)
        
        self.sign_in_label = Label(self.lgn_frame, text=f'Earnings : ₹{database.getEarnings()}', bg="blue", fg="white", font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=150)
        
        # self.sign_in_label = Button(self.lgn_frame, text="ADD RACKS", bg="blue", fg="white",command=self.racks,
        #                             font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        # self.sign_in_label.place(x=480, y=470)
        
        # /////////////////////////////////////////////////////////////////////////
        # # ///////////////////////////////GO BACK PHOTO ////////////////////////////
        # # //////////////////////////////////////////////////////////////////////////
        # self.lgn_button = Image.open('resized images\\back1.png')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Button(self.lgn_frame, image=photo, bg='#040405')
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=0, y=0)




        
    def addbook(self):
        obj = add_book.AddBook(self.window)
        
        
    # def addorder(self):
    #     obj = order_list.page()
        
    def addcategory(self):
        obj = category.Category(self.window)
        # obj=add_book.page()
        # add_book.AddBook(self.window)
    def addemployee(self):
        obj = add_employee.ADDEmployee(self.window)
        
    def viewemployee(self):
        obj = employee_tables.EmployeeTables()
        obj.ViewEmployee()
        
    # def vieworders(self):
    #     obj = order_tables.OrderTables()
    #     obj.ViewOrders()
         
    def bills(self):
        obj=bill1.Bills()
        obj.billing()         
        
    def racks(self):
        obj=racks.page()
           
        

#obj=login_page_window(root)       
        # obj2=bill.login_page_window(self)        
        # root.mainloop()
        
    def viewbook(self):
       obj = edit_books_tables.EditBooksTables()
       obj.EditBOOKS()
       
    def viewracks(self):
       obj = racks_tables.RacksTables()
       obj.ViewRacks()
    
    def viewCategories(self):
       obj = categories_tables.viewcategory()
       obj.category()
       
    def booktables(self):
       obj = edit_books_tables.EditBooksTables()
       obj.EditBOOKS()
        
    def openBills(self):
        obj = viewOrders.viewOrders()
        obj.ViewEmployee()


def page():
    window = Toplevel()
    menupage(window)
    window.mainloop()


if __name__ == '__main__':
    page()