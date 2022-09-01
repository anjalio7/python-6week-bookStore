

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from email import message
import add_book
import book_tables
import add_employee
import employee_tables
import racks
import racks_tables
import category
import categories_tables, empGenerateBill

class menupage:
    def __init__(self, window, res):

        self.id = res

        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('BOOK STORE MANAGEMENT SYSTEM')
        
        
        
       # ========================================================================
        # ================================    MENU BAR   =======================
        # ========================================================================
        
        
        self.menubar = Menu(self.window)  
        self.file = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file.add_command(label="view categories",command=self.CategoryTable )  
        self.file.add_command(label="Delete Books")  
        self.file.add_command(label="Views Books")  
        self.file.add_command(label="Total Earnings")  
        self.file.add_command(label="View Bills")  
  
        self.file.add_separator()  
  
        self.file.add_command(label="Exit", command=self.window.quit)  
  
        self.menubar.add_cascade(label="Options", menu=self.file)  
        self.edit = Menu(self.menubar, tearoff=0)  
        self.edit.add_command(label="Undo")  

  
        # self.window.config(menu=self.menubar)  
        

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

 
        self.txt = "EMPLOYEE MENU  "
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
        self.side_image_label.place(x=5, y=160)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_label = Button(self.lgn_frame, text="GENERATE BILL", bg="BLUE", fg="white",command=self.generateBill,
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=150)


        
        self.sign_in_label = Button(self.lgn_frame, text="Logout", bg="BLUE", fg="white",command=self.window.destroy,
                                    font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        self.sign_in_label.place(x=480, y=230)
        
        # self.sign_in_label = Button(self.lgn_frame, text="ADD CATEGORY", bg="BLUE", fg="white",command=self.category,
        #                             font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        # self.sign_in_label.place(x=480, y=310)
        
        # self.sign_in_label = Button(self.lgn_frame, text="GENERATE BILL FOR CUSTOMER ", bg="BLUE", fg="white",
        #                             command=self.bills,font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        # self.sign_in_label.place(x=480, y=390)
        
        # self.sign_in_label = Button(self.lgn_frame, text="ADD RACKS", bg="BLUE", fg="white",command=self.racks,
        #                             font=("yu gothic ui", 17, "bold") , height= 1, width=30)
        # self.sign_in_label.place(x=480, y=470)

    # def addbook(self):
    #     obj = add_book.AddBook(self.window)
    

    def generateBill(self):
        obj = empGenerateBill.EmpBill()
        obj.billing(self.id) 

    def addbook(self):
        # obj = add_book.AddBook(self.window)
        add_book.page()
        # obj=add_book.page()
        # add_book.AddBook(self.window)


         
    # def bills(self):
    #     bill.page()                
        
    def racks(self):
        obj=racks.page()
  
    def category(self):
        obj=category.page()

           
        

#obj=login_page_window(root)       
        # obj2=bill.login_page_window(self)        
        # root.mainloop()
        
    def viewbook(self):
       obj = book_tables.BooksTables()
       obj.BOOKS()
       
    def viewracks(self):
       obj = racks_tables.BooksTables()
       obj.ViewBook()
       
    def booktables(self):
       obj = book_tables.BooksTables()
       obj.BOOKS()
        
    def CategoryTable(self):
       obj = categories_tables.viewcategory()
       obj.category()
        
        


def page():
    window = Toplevel()
    menupage(window)
    window.mainloop()


if __name__ == '__main__':
    page()