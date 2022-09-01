
from tkinter import *
from tkinter.ttk import Treeview
# from .database import AddEmployee
import database
import add_employee
import employee_tables
from tkinter import messagebox
import employee_edit
class EmployeeTables():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('EMPLOYEE DETAILS')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2 )
        self.height=int((self.fullheight-500)/2)

        s = "1000x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def ViewEmployee(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=25,stretch=NO)

        self.tr.heading('#1',text="EMPLOYEE NAME")
        self.tr.column('#1',minwidth=0,width=170 ,stretch=NO)

        self.tr.heading('#2', text="EMAIL")
        self.tr.column('#2', minwidth=0, width=170, stretch=NO)
        
        self.tr.heading('#3', text="PHONE NO.")
        self.tr.column('#3', minwidth=0, width=170, stretch=NO)

        self.tr.heading('#4', text="USERNAME")
        self.tr.column('#4', minwidth=0, width=170, stretch=NO)

        # self.tr.heading('#5', text="PASSWORD")
        # self.tr.column('#5', minwidth=0, width=170, stretch=NO)
        
        self.tr.heading('#5', text="Edit")
        self.tr.column('#5', minwidth=0, width=30, stretch=NO)

        self.tr.heading('#6', text="Delete")
        self.tr.column('#6', minwidth=0, width=50, stretch=NO)


        self.tr.place(x=0,y=0,width="1000",height="500")

        j = 0
        # print("manage",database.allEmployees)
        for i in database.allEmployees():
            self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],i[4],'Edit','Delete'))        

        self.tr.bind('<Double-Button-1>', self.actions)
        res = database.allEmployees()
        # if res:
        #     print(res)
        #     # if len(res) > 0:
        #     #     for i in res:
        #     #         self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3],i[4],i[5],i[6], 'Edit', 'Delete'))
        # else:
        #     messagebox.showerror("'alert',no books to show")
        # else:
        #     messagebox.showerror('Alert', 'Soemthing went wrong')

        self.root.mainloop()

    def actions(self,e):
        #get the values of the selected row
        tt=self.tr.focus()

        #get the column Id
        col= self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        id=(
            self.tr.item(tt).get('text'),
        )

        print(id, col)
        if col == '#6':
            a = messagebox.askyesno('Alert', 'Do you really want to delete it?')
            if a:
                res = database.deleteemployee(id)
                if res:
                    messagebox.showinfo('Success', 'student deleted successfully.')
                    self.root.destroy()
                    obj = employee_tables.EmployeeTables()
                    obj.ViewEmployee()                    
                else:
                    messagebox.showerror('Alert', 'Somethng went wrong.')

        if col == '#5':
            obj= employee_edit.page(id)


        # self.root.mainloop()
if __name__ == '__main__':
    obj = EmployeeTables()
    obj.ViewEmployee()